@echo off
for %%I in (%cd%) do title %%~nI
call conda activate
flask --app test run
pause