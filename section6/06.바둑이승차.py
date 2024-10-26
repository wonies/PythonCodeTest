import sys
sys.stdin = open("inputs/06.txt", "rt")


def DFS(i, cur_weight, arr, tot):
    global max_weight
    if (cur_weight > tot):
        return
    if (i == len(arr)):
        if cur_weight > max_weight:
            max_weight = cur_weight
    else:
        DFS(i + 1, cur_weight + arr[i], arr, tot)
        DFS(i + 1, cur_weight, arr, tot)    

n, m = map(int, input().split())
a = list(map(int, input().split()))
# ch = [0] * (m + 1)

max_weight = 0
DFS(0, 0, a, n)
print("max weight: ", max_weight)