import sys, os, screen, threading, time
def current_path():
    return os.path.abspath(os.sep)
def putfiles(cur_path : str):
    screen.pusht(0,0,"----------------------------------------------------------------", False)
    for i in range(1, 29):
        screen.pusht(0, i, "|                                                              |", False)
    screen.pusht(0,29,"----------------------------------------------------------------", False)
    dir=(os.listdir(cur_path))
    x=1
    for i in dir:
       screen.pusht(1, x, i, False)
       x+=1
       if x > 27:
           screen.apop(1, x, 62)
           screen.pusht(1,x,"more not shown...", False)
           break
    
    screen.updscn()
path = current_path()
putfiles(path)
while True:
    d = screen.getkey()
    if d == "up":
        os.chdir("..")
        path = os.getcwd()
        putfiles(path)
    elif d == "c":
        screen.kscnpipe(0, 31)
        npath = screen.apeek(0, 31, 64, False).strip()
        try:
            os.listdir(npath)
            path = npath
            putfiles(path)
            os.chdir(path)
        except OSError as a:
            pass
        putfiles(path)
        screen.apop(0,31,64)
    elif d == "r":
        screen.kscnpipe(0, 31)
        npath = path + screen.apeek(0, 31, 64, False).strip() + os.sep
        try:
            os.listdir(npath)
            path = npath
            putfiles(path)
            os.chdir(path)
        except OSError as a:
            pass
        putfiles(path)
        screen.apop(0,31,64)
    elif d == "esc":
        exit()
