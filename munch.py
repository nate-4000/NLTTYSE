import screen
import time
def munch(d):
    for i in range(0, 32):
        screen.pushp(i, i^d, "#", False)
    screen.updscn()
for i in range(32):
    munch(i)
    time.sleep(0.5)