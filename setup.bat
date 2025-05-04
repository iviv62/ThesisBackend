@echo off
echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call .\venv\Scripts\activate

echo Installing project in development mode...
pip install -e .

echo Setup complete! The virtual environment is now activated.
echo You can run the application with:
echo uvicorn main:app --reload

rem Keep the virtual environment activated
cmd /k 