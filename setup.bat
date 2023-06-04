@echo off
setlocal

REM Prompt the user with a choice to import colors from the configuration folder
echo Would you like to import colors from the configuration folder?
choice /t 4 /d n /n >nul
if errorlevel 2 (
    echo Skipping color import.
) else (
    REM Copy color_config.json to colors.json
    copy /y ".\config\color_config.json" ".\main\colors.json"
)

REM Change directory to the main folder
cd /d ".\main"

REM Run the Python scripts
python utils\generate_triggers.py
python utils\generate_icons.py

endlocal

pause