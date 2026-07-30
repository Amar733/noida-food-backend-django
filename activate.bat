@echo off
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Virtual environment activated!
echo.
echo You can now run:
echo   python manage.py makemigrations
echo   python manage.py migrate
echo   python manage.py createsuperuser
echo   python manage.py runserver
echo.
cmd /k
