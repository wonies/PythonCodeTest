import sys
sys.stdin = open("04.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
m = int(input())
k = list(map(int, input().split()))

p1 = p2 = 0
arr = []
i = 0

while p1 < n and p2 < m:
    if (a[p1] < k[p2]):
        arr.append(a[p1])
        p1+=1
    else:
        arr.append(k[p2])
        p2+=1
if (p1 < n):
    arr = arr + a[p1:]
else:
    arr = arr + k[p2:]

for x in arr:
    print(x, end=' ')
    