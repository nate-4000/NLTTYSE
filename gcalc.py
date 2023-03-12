import screen

screen.sy = 32
screen.sx = 20

screen.pusht(0,0, "----------------------", False)
screen.pusht(0,1, "|                    |", False)
screen.pusht(0,2, "----------------------", False)

screen.pusht(0,4, "----------------------", False)
screen.pusht(0,5, "|                    |", False)
screen.pusht(0,6, "----------------------", False)

screen.pusht(0,8, "[i]: input            ", False)
screen.pusht(0,9, "[c]: calculate        ", False)
screen.pusht(0,10,"[\u241b]: exit             ", False)

oper = ''

screen.updscn()

while True:
    d = screen.getkey()

    if d == 'esc':
        break
    elif d == 'i':
        screen.kscnpipe(1, 1, 20)
        oper = screen.apeek(1, 1, 20)
    elif d == 'c':
        try:
            out = eval(oper)
        except BaseException as e:
            out = e
        screen.apop(1,5,20)
        screen.pusht(1,5, str(out)[:20])