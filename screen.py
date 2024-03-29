"""
A library for emulating a screen in a terminal using letterpixels.
Letterpixels are not pixels in the normal sense, only letters in a grid acting as such.

scnmem: The screen memory
sx: The screen's length in letterpixels
sy: the screen's height in letterpixels
"""

scnmem = []
sx = 64
sy = 32
import os
import keyboard
def cls():
    """Clears the terminal on most systems."""
    if os.name == "nt":
        os.system("cls")
    else:
        print("\033[2J\033[H")
        #os.system("clear") # IF ANSI'ING IT DONT WORK UNCOMMENT IT AND RECOMPILER KERNAL #(note from other dev, dont, too much work and most people are stupid) 
def pushp(x, y, t="\u2588", r=True):
    """Pushes a pixel to the screen."""
    global scnmem
    popp(x, y)
    scnmem += [[x, y, t]]
    if r:
        updscn()
def clrscn():
    """Clears the screen memory. Requires an update afterwards for compatibility."""
    global scnmem
    scnmem = []
def peekp(x, y, pn=False):
    """Grabs what pixel is at (x, y) on the screen. If pn (preserve null) is on, gives None when there is no pixel there."""
    global scnmem
    for i in scnmem:
        if i[0] == x and i[1] == y:
            return i[2]
    if pn:
        return None
    else:
        return " "
def pescnmem(x,y):
    """Checks if a pixel exists."""
    global scnmem
    for i in scnmem:
        if i[0] == x and i[1] == y:
            return True
    return False
def popp(x,y):
    """Pops a pixel from the screen at the specified position."""
    global scnmem
    for i in scnmem:
        if i[0] == x and i[1] == y:
            scnmem.remove(i)
def updscn():
    """Updates the screen."""
    cls()
    global scnmem
    l = ""
    for y in range(0, sx):
        for x in range(0, sy):
            if pescnmem(x, y):
                d = peekp(x, y)
                l += d
            else:
                l += " "
        l += "\n"
    print(l)
def pusht(x, y, t, u = True):
    """Pushes text to the screen. \"u\" is the update flag."""
    lt = list(t)
    h = 0
    for rt in lt:
        pushp(x+h, y, rt, False)
        h+=1
    if u:
        updscn()
def getkey():
    """Basically a wrapper for \"keyboard.readkey()\""""
    return keyboard.read_key(True)
def kscnpipe(x, y, l=64):
    """Handles textboxes. \"l\" is the length of the textbox."""
    apop(x, y, l)
    updscn()
    stop = False
    offset = 0
    while not stop:
        k = getkey()
        if k == "enter":
            stop = True
            break
        elif k == "space":
            pushp(x+offset, y, " ")
            offset += 1
            offset = abs(offset)
        elif k == "backspace":
            offset -= 1
            offset = abs(offset)
            popp(x+offset, y)
            updscn()
        elif len(k) != 1:
            pass
        else:
            pushp(x+offset, y, k)
            offset += 1
            offset = abs(offset)
        if offset >= l:
            return
def apeek(x, y, le, pn=False):
    """Peeks an area of the screen. Good for getting what the user typed using \"kscnpipe()\". PN flag provided for compatiblity."""
    out = ""
    for i in range(le):
        out += peekp(x+i, y)
    return out
def apop(x, y, le):
    """Pops an area from the screen."""
    pusht(x, y, " "*le)
