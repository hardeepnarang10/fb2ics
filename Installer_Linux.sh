#!/bin/bash
set echo off
printf "\ec"
cd "$(dirname "$0")"
echo
echo Installing Prerequisites...
echo
pip3 install -q -r requirements.txt
echo Done!
echo
echo Executing fb2ics...
python3 fb2ics.py
read -p "Press any key to exit."
exit