python 3.10
linux:
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt 

- pip freeze -l
- pip freeze -l > requirements.txt

windows:
- py -m venv venv
- venv\Scripts\activate.bat

Windows PowerShell (VS code)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\Activate.ps1
