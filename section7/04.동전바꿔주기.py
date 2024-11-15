import sys
sys.stdin = open("inputs/04.txt")

def DFS(level, sumval):
    global cnt
    if (sumval == T):
        cnt += 1
        return 
    if (sumval > T or level == k):
        return
    else:
        for i in range(coincnt[level] + 1):
            DFS(level + 1, sumval + coinvalue[level] * i)

T = int(input())
k = int(input())
coinvalue = list()
coincnt = list()
for _ in range(k):
    a,  b =map(int, input().split())
    coinvalue.append(a)
    coincnt.append(b)
cnt = 0
DFS(0, 0)
print(cnt)