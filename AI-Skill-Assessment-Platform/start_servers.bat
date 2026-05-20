@echo off
echo Starting AI Skill Assessment Platform Servers...

:: Start the Backend Server in a new window
echo Starting Backend Server...
start cmd /k "title Backend Server && cd backend && call .\venv\Scripts\activate.bat && python manage.py runserver"

:: Start the Frontend Server in a new window
echo Starting Frontend Server...
start cmd /k "title Frontend Server && cd frontend && npm run dev"

echo Both servers are starting up in separate windows!
