import sys
import math
num = int(sys.stdin.readline().rstrip())
skill = []
for i in range(num):
    skill.append(list(map(int,sys.stdin.readline().rstrip().split())))
A_team = []
team_score = []
exit = 0
visit = [0]*num
def cal_score(B_team):
    A_score = 0
    B_score = 0
    for i in range(len(A_team)-1):
        for j in range(i,len(A_team)):
            A_score += skill[A_team[i]][A_team[j]]+skill[A_team[j]][A_team[i]]
            B_score += skill[B_team[i]][B_team[j]] + skill[B_team[j]][B_team[i]]
    if A_score > B_score:
        return A_score-B_score
    else:
        return B_score-A_score

def team(cnt,cur):
    global exit,A_team
    if cnt == num//2:
        cnt = 0
        exit += 1
        B_team = []
        for i in range(num):
            if i not in A_team:
                B_team.append(i)
        team_score.append(cal_score(B_team))
        if exit == math.factorial(num)//math.factorial(num//2)//math.factorial(num//2):
            print(min(team_score))
            sys.exit()
    else:
        for i in range(cur,num):
            if visit[i]==1:
                continue
            visit[i] = 1
            A_team.append(i)
            team(cnt+1,i)
            visit[i] = 0
            A_team.pop()

team(0,0)