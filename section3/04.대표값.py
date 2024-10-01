import sys
sys.stdin = open("05.txt", "rt")

N = int(input())
a = list(map(int, input().split()))
total = sum(a)
avg = round(total / N)
min = float('inf')
res_score = -1
res_idx = -1

for i in range(N):
    diff = abs(a[i] - avg)
    if (diff < min):
        min = diff
        res_score = a[i]
        res_idx = i + 1
    elif diff == min:
        if (a[i] > res_score):
            res_score = a[i]
            res_idx = i + 1

print(avg, res_idx)