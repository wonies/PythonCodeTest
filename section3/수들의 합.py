import sys
sys.stdin = open("05.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
goal = 0
for i in range(n):
    goal +=  a[i]
    if (a[i] == m):
        cnt += 1
        goal = 0
    if (goal == m):
        cnt += 1
        goal = a[i]
print(cnt)