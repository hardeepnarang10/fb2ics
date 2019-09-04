@echo off
cd %~pd0
echo.
echo.
echo Installing Prerequisites...
echo.
pip3 install -q -r requirements.txt
echo Done!
echo.
echo Executing fb2ics...
python fb2ics.py
echo Press any key to exit.
pause>nul
exit