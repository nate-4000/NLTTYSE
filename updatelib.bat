REM put the cwd in python's lib directory so that we can import from other scripts
CD %LocalAppData%\Programs\Python\Python311\Lib
REM copy the file there
REM wtf is %~dp0
REM "." dont work, but why?
COPY %~dp0\screen.py %LocalAppData%\Programs\Python\Python311\Lib