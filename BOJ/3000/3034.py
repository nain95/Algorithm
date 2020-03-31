import sys
n,w,h =  map(int,sys.stdin.readline().split())
for _ in range(n):
    tmp = int(sys.stdin.readline())
    if tmp <= w or tmp <= h or tmp <= pow(pow(w,2)+pow(h,2),0.5):
        print("DA")
    else:
        print("NE")