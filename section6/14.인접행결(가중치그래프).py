import sys
sys.stdin = open("inputs/14.txt", "rt")

n, m = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n + 1)]

for _ in range(m):
    k = list(map(int, input().split()))
    graph[k[0] - 1][k[1] - 1] = k[2]
    
for i in range(n):
    for j in range(n):
        print(graph[i][j], end=" ")
    print()