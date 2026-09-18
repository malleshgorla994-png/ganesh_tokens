Set objShell = CreateObject("WScript.Shell")
objShell.Run "cmd.exe /k ""pip install flask pillow && echo. && echo [OK] Installation complete! && echo. && pip show flask && pip show pillow""", 1, False
