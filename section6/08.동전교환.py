import sys
sys.stdin = open("inputs/08.txt", "rt")

def DFS(i,cnt,arr, tot):
    global min_cnt
    if (tot > k):
        return
    if (i == len(arr)):
        if (min_cnt > cnt):
            min_cnt = cnt
    else:
        DFS(i + 1, cnt + 1, arr, tot + arr[i])
        # DFS(i + 1, cnt + 1, arr, tot)
            

n = int(input())
a = list(map(int, input().split()))
k = int(input())
min_cnt = 2147000000
DFS(0, 0, a, 0)
print("min cnt" , min_cnt)