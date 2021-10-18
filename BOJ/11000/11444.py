import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def fibonacci(n):
    if n in dic:
        return dic[n]
    elif n % 2 == 0:
        m = n // 2
        if m not in dic:
            temp1 = fibonacci(m)
        else:
            temp1 = dic[m]
        if m-1 not in dic:
            temp2 = fibonacci(m-1)
        else:
            temp2 = dic[m-1]
        result = (2 * temp2 + temp1) % mod * temp1 % mod
        return result
    else:
        m = n // 2
        if m + 1 not in dic:
            temp1 = fibonacci(m + 1)
        else:
            temp1 = dic[m + 1]
        if m not in dic:
            temp2 = fibonacci(m)
        else:
            temp2 = dic[m]
        result = ((temp1 ** 2 % mod) + (temp2 ** 2 % mod)) % mod
    dic[n] = result
    return result

mod = 1000000007 
n = int(sys.stdin.readline())
dic = defaultdict(int)
dic[0] = 0
dic[1] = 1
ans = fibonacci(n)
print(ans % mod)
