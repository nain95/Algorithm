import sys
from collections import defaultdict

tmp_list = []
tmp = sys.stdin.readline().rstrip()
dic = defaultdict(int)
count = 0
while tmp:
    dic[tmp] += 1
    count += 1
    tmp = sys.stdin.readline().rstrip()
for key in sorted(dic.keys()):
    print("%s %.4f" %(key,dic[key]/count*100))