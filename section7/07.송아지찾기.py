import sys
sys.stdin = open("inputs/06.txt", "rt")

def DFS(cnt, step):
    global min_cnt
    if (cnt >= min_cnt):
        return 
    if (step == m):
        min_cnt = min(min_cnt, cnt)
        return 
    if (step > m + 5 or step < 0):
        return 
    else:
        DFS(cnt + 1, step + 1)
        DFS(cnt + 1, step - 1)
        DFS(cnt + 1, step + 5)
        
    
    
    
n, m = map(int, input().split())
min_cnt = 214700000
DFS(0, n)
print("min cnt : ", min_cnt)