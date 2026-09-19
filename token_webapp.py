"""
Web UI for jj.py's token registration flow.

Run with:
    python token_webapp.py

Then open the printed "Network" link on any device on the same Wi-Fi to
fill the form and get a token. Data is stored in SQLite (tokens.db) under
~/TokenReceipts (or TOKEN_DIR env var on cloud). Receipt images are
generated on-the-fly in memory — no disk writes required for the web app.
"""

import base64
import io
import os
import socket
import threading

from flask import Flask, abort, redirect, render_template, request, send_file, url_for

import jj

ORG_NAME = "Gadi Maisamma Youth, Yerrambelly"

app = Flask(__name__)
_submit_lock = threading.Lock()


def _valid_phone(phone):
    return phone.isdigit() and len(phone) >= 10


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", org_name=ORG_NAME)


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()

    if not name:
        return render_template("index.html", org_name=ORG_NAME, error="Name cannot be empty.", name=name, phone=phone), 400
    if not _valid_phone(phone):
        return render_template(
            "index.html", org_name=ORG_NAME,
            error="Please enter a valid phone number (digits only, at least 10 digits).",
            name=name, phone=phone,
        ), 400

    with _submit_lock:
        created_by = request.form.get("created_by", "").strip()
        token_no, timestamp = jj.save_token(name, phone, created_by)
        try:
            image_path = os.path.join(jj.SAVE_DIR, f"receipt_{token_no}.png")
            jj.build_receipt_image(token_no, name, phone, timestamp, image_path)
        except Exception:
            pass

    return redirect(url_for("receipt", token_no=token_no))


@app.route("/receipt/<int:token_no>")
def receipt(token_no):
    record = jj.lookup_token(token_no)
    if record is None:
        abort(404)
    return render_template(
        "receipt.html",
        token=record["token"],
        name=record["name"],
        phone=record["phone"],
        timestamp=record["timestamp"],
    )


@app.route("/admin")
def admin():
    """Admin page — shows all registered tokens from the database."""
    tokens = jj.get_all_tokens()
    next_token = jj.get_next_token_number()
    return render_template("admin.html", tokens=tokens, org_name=ORG_NAME, next_token=next_token)


@app.route("/admin/delete/<int:token_no>", methods=["POST"])
def delete_token(token_no):
    """Delete a single token record from the database."""
    jj.delete_token_by_no(token_no)
    return redirect(url_for("admin"))



@app.route("/receipt-image/<int:token_no>.png")
def receipt_image(token_no):
    record = jj.lookup_token(token_no)
    if record is None:
        abort(404)
    # Generate receipt image in memory — works on any cloud platform
    buf = jj.build_receipt_image_bytes(
        record["token"], record["name"], record["phone"], record["timestamp"]
    )
    return send_file(buf, mimetype="image/png")


@app.route("/logo.jpg")
def logo():
    for path in jj.LOGO_OVERRIDE_PATHS:
        if os.path.exists(path):
            return send_file(path)
    raw = base64.b64decode(jj.DEFAULT_LOGO_B64)
    return send_file(io.BytesIO(raw), mimetype="image/jpeg")


def _lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


if __name__ == "__main__":
    jj.init_db()   # create tokens table if it doesn't exist yet
    ip = _lan_ip()
    port = int(os.environ.get("PORT", 5000))
    print(f"Database: {jj.DB_FILE}")
    print(f"Local:   http://127.0.0.1:{port}")
    print(f"Network: http://{ip}:{port}   <- share this with your group on the same Wi-Fi")
    app.run(host="0.0.0.0", port=port, threaded=True)
