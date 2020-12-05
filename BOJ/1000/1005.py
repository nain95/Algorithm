import sys
class solve():
    def __init__ (self):
        self.max = 30
        self.save = [[0] * self.max for i in range(self.max)]
    def bridge_cnt(self,n,m):
        if self.save[n][m] != 0:
            return self.save[n][m]

        for i in range(n-1,m):
            self.save[n][m] += self.bridge_cnt(n-1,i)
        return self.save[n][m]

    def main(self):
        for i in range(1,30):
            self.save[1][i] = i
        t = int(sys.stdin.readline())
        for i in range(t):
            n,m = tuple(int(i) for i in sys.stdin.readline().split())
            print(self.bridge_cnt(n,m))
if __name__ == "__main__":
    s = solve()
    s.main()
