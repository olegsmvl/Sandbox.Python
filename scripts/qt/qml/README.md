python3 -m venv venv
source venv/bin/activate
pip freeze -l > requirements.txt
deactivate
pip install -r requirements.txt 
py main.py -c conf_can.toml

windows
py -m venv venv
venv\Scripts\activate.bat

PowerShell (console VS Code)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\Activate.ps1

///////
1. connect can
