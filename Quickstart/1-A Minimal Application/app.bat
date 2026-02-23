@echo off
for %%I in (%cd%) do title %%~nI
call conda activate
flask run --host=0.0.0.0