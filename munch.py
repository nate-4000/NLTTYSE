import screen
import time
screen.sx = 32
screen.sy = 32
def munch(d):
    for i in range(0, 32):
        screen.pushp(i, i^d, "#", False)
    screen.updscn()
for i in range(32):
    munch(i)
    time.sleep(0.2)