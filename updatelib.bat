REM put the cwd in python's funni place for funni reasons
CD %LocalAppData%\Programs\Python\Python310\Lib
REM copy the file there
REM wtf is %~dp0
REM "." dont work, but why?
COPY %~dp0\screen.py %LocalAppData%\Programs\Python\Python310\Lib