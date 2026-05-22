@echo off
echo Starting TinyLlama 1.1B CPU version...
start /b ollama serve
timeout /t 2 /nobreak >nul
python app.py
pause
