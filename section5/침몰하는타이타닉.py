import sys
sys.stdin = open("08.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
greedy = -2147000000
idx = 0
cnt = 0

while (len(a) > 1):
    idx = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            temp = a[i] + a[j]
            if (temp > greedy and temp <= m):
                greedy = temp
                idx = j - 1
                cnt += 1
    a.pop(idx)
    

print("cnt : ", cnt)