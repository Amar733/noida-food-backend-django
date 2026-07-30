Write-Host "Activating virtual environment..." -ForegroundColor Green
.\venv\Scripts\Activate.ps1
Write-Host "Virtual environment activated!" -ForegroundColor Green
Write-Host ""
Write-Host "You can now run:" -ForegroundColor Yellow
Write-Host "  python manage.py makemigrations" -ForegroundColor Cyan
Write-Host "  python manage.py migrate" -ForegroundColor Cyan
Write-Host "  python manage.py createsuperuser" -ForegroundColor Cyan
Write-Host "  python manage.py runserver" -ForegroundColor Cyan
Write-Host ""
