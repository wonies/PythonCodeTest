import sys
sys.stdin = open("inputs/09.txt", "rt")


def DFS(level):
    global cnt
    if (level == m):
        if(res[0] == res[1]):
            return 
        cnt += 1
        print(" ".join(map(str, res[:m])))
    else:
        for i in range(1, n+1):
            res[level] = i
            DFS(level+1)
        
        

n, m = map(int, input().split())
res = [0] * m
cnt = 0
DFS(0)
print(cnt)

#순열은 check해서 푼다.
