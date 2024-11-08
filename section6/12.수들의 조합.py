import sys
sys.stdin = open("inputs/12.txt", "rt")

def DFS(level, start, sum):
    global cnt
    if (level == m):
        if (sum % multiple == 0):
            cnt += 1
    else:
        for i in range(start, n):
            DFS(level + 1, i + 1, sum + k[i])
            
    
n, m = map(int, input().split())
k = list(map(int, input().split()))
multiple = int(input())

arr = [0] * m
cnt = 0
DFS(0, 0, 0)
print("cnt: ", cnt)