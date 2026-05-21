@echo off
cd /d "%~dp0"
echo Starting dev server at http://localhost:8080
"C:\Users\USER\AppData\Local\Python\pythoncore-3.14-64\python.exe" serve.py
pause
