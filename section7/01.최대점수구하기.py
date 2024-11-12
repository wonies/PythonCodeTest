import sys
sys.stdin = open("inputs/01.txt", "rt")


def DFS(level, tot, ttime):
    global scores
    if (ttime > m):
        print(f"DFS 호출: level={level}, tot={tot}, ttime={ttime}")
        return
    if (level == n):
        scores = max(scores, tot)
        return 
    else:
        DFS(level + 1, score[level] + tot, ttime + times[level])
        DFS(level + 1, tot, ttime)
        


n, m = map(int, input().split())
score = [0] * n
times = [0] * n
scores = -2147900000

for i in range(n):
    a, b = map(int, input().split())
    score[i] = a
    times[i] = b

DFS(0, 0, 0)
print("scores : ", scores)
