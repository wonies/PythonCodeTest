import sys
sys.stdin = open("inputs/03.txt", "rt")


def DFS(index, cur_weight, arr, res):
    if (index==len(arr)):
        res.add(cur_weight)
        return
    else:
        DFS(index + 1, cur_weight + arr[index], arr, res)
        DFS(index + 1, abs(cur_weight - arr[index]), arr, res)
        DFS(index + 1 , cur_weight, arr, res)


k = int(input())
a = list(map(int, input().split()))
sum_a = sum(a)
res = set()
DFS(0, 0, a, res)
cnt = 0 
for i in range(1, sum_a + 1):
    if i not in res:
        cnt += 1
print(cnt)