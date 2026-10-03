@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (
    py -3 download_apps.py --all
) else (
    where python >nul 2>nul
    if errorlevel 1 (
        echo Installa Python 3.9 o superiore da https://www.python.org/downloads/windows/
        echo Abilita Add Python to PATH durante l'installazione.
        pause
        exit /b 1
    )
    python download_apps.py --all
)
set download_result=%errorlevel%
pause
exit /b %download_result%
