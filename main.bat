
:: Check for Python Installation
python --version 2>NUL
if errorlevel 1 goto errorNoPython

cmd /c "pip install -r requirements.txt"

cmd /c "main.py"


:errorNoPython
echo.
cmd /c "python-3.9.0.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0"

cmd /c "pip install -r requirements.txt"

cmd /c "main.py"