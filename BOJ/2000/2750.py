N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))
data = sorted(data)
for i in data:
    print(i)