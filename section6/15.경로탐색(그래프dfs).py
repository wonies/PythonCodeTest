import sys
sys.stdin = open("inputs/15.txt", "rt")

n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b =  map(int, input().split())
    graph[a-1][b-1] = 1

def DFS(start, end):
    global cnt
    if (start == end):
        cnt += 1
        return 
    visited[start] = True
    for i in range(n):
        if (graph[start][i] == 1 and not visited[i]):
            DFS(i, end)
    visited[start] = False

cnt = 0
visited = [False] * n
DFS(0, n-1)
print(cnt)