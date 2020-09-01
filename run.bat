@echo off
call C:\Users\wuwei\AppData\Local\Programs\Python\Python38\python.exe ".\math_test.py"


if not %ERRORLEVEL% == 0 (
    pause
    
)

