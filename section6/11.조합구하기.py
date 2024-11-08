import sys

sys.stdin = open("inputs/11.txt", "rt")



def DFS(level, start):
    global cnt
    if (level == m):
        print(*res)
        cnt += 1
        return
    else:
        for i in range(start, n+1):
            res[level] = i
            DFS(level + 1, i + 1)    
        


n, m = map(int, input().split())

res = [0] * m
ch = [0] * m

cnt = 0
DFS(0, 1)
print(cnt)