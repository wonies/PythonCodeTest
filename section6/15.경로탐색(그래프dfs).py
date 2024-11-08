import sys
sys.stdin = open("inputs/15.txt", "rt")

n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b =  map(int, input().split())
    graph[a-1][b-1] = 1

def DFS(start, next, end):
    global cnt
    if (next == end):
        print("start, end", start, end)
        cnt += 1
        return 
    else:
        for i in range(start, end + 1):
            if (graph[i][next] == 1):
                DFS(next, next + 1, end)
            else:
                DFS(start + 1, next, end)

cnt = 0
DFS(0, 1, n)
print(cnt)