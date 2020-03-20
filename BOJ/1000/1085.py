import sys
x,y,w,h = map(int,sys.stdin.readline().split())
print(min(min(w-x,x),min(h-y,y)))