# Token Registration App — Setup Guide
## Gadi Maisamma Youth, Yerrambelly

---

## What does this app do?

A local web app where people fill their **Name + Phone number** and get a numbered **token receipt** (shown on-screen + saved as a PNG image). It works on this laptop and any phone/tablet on the **same Wi-Fi**.

---

## Folder structure (after setup)

```
token\
├── SETUP.bat           ← Run ONCE to install dependencies
├── START_APP.bat       ← Run every time to start the app
├── token_webapp.py     ← Main Flask web app
├── jj.py               ← Receipt/token logic
├── templates\
│   ├── base.html
│   ├── index.html
│   └── receipt.html
```

Receipts and the token list are saved in:
```
C:\Users\<YourName>\TokenReceipts\
    tokens.csv          ← All token records
    receipt_1.png
    receipt_2.png
    ...
```

---

## Step 1 — Install Python (one time only)

1. Go to **https://www.python.org/downloads/** and download the latest Python 3.x installer.
2. Run the installer.
3. ✅ **Check the box "Add Python to PATH"** before clicking Install.

---

## Step 2 — Run SETUP.bat (one time only)

Double-click **`SETUP.bat`** in the `token` folder.

It will:
- Confirm Python is installed
- Install **Flask** and **Pillow** (the two required libraries)

You only need to do this once.

---

## Step 3 — Start the app

Double-click **`START_APP.bat`** every time you want to run the app.

A black command window will open and show something like:

```
Token file: C:\Users\User\TokenReceipts\tokens.csv
Local:   http://127.0.0.1:5000
Network: http://192.168.1.10:5000   <- share this with your group
```

- **This laptop**: open http://127.0.0.1:5000 in a browser
- **Phones/tablets on the same Wi-Fi**: use the `Network:` URL

---

## Step 4 — Stop the app

Close the black command window, or press **Ctrl + C** inside it.

---

## Optional — Custom logo

Place a file named **`logo_override.jpg`** (or `.png`) inside the `TokenReceipts` folder to replace the default logo on all receipts.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| "Python not found" | Re-install Python and tick "Add to PATH" |
| "No module named flask" | Run `SETUP.bat` again |
| App starts but can't open in browser | Try http://127.0.0.1:5000 directly |
| Phone can't reach the Network URL | Make sure laptop and phone are on same Wi-Fi |
