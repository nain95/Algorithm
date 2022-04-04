for _ in range(3):
    a, b, c, d, e, f = map(int, input().split())
    i = (60 + f - c) % 60
    if f - c < 0:
        e -= 1
    h = (60 + e - b) % 60
    if e - b < 0:
        d -= 1
    g = (24 + d - a) % 24
    print(g, h, i)