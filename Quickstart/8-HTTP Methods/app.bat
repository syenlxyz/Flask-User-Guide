@echo off
for %%I in (%cd%) do title %%~nI
call conda activate
flask run
pause