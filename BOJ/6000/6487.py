import sys

n = int(sys.stdin.readline())
for _ in range(n):
    ch1, ch2 = 0, 0
    x1,y1,x2,y2,x3,y3,x4,y4 = list(map(int, sys.stdin.readline().split()))
    if x1 == x2:
        inclination1 = 0
        ch1 = 1
    else:
        inclination1 = (y2 - y1) / (x2 - x1)
    if x3 == x4:
        inclination2 = 0
        ch2 = 1
    else:
        inclination2 = (y4 - y3) / (x4 - x3)
    b1 = y1 - (inclination1 * x1)
    b2 = y3 - (inclination2 * x3)
    if (ch1 + ch2) % 2 == 0 and inclination1 == inclination2:
        if b1 == b2 or (ch1 + ch2 == 2 and x1 == x3):
            print("LINE")
        else:
            print("NONE")
    elif (ch1 + ch2) == 1 and inclination1 == inclination2:
        if ch1 == 1:
            x = x1
            y = y3
        else:
            x = x3
            y = y1
        print(f"POINT {round(x, 2):.2f} {round(y, 2):.2f}")
    else:
        x = (b2 - b1) / (inclination1 - inclination2)
        y = inclination2 * x + b2
        if x == 0:
            x = 0
        if ch1 + ch2 == 1:
            if inclination2 == 0:
                x = x3
                y = inclination1 * x + b1
            elif inclination1 == 0:
                x = x1
                y = inclination2 * x + b2
        print(f"POINT {round(x, 2):.2f} {round(y, 2):.2f}")
