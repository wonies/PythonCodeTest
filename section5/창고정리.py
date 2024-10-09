import sys
sys.stdin = open("07.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    max_idx = a.index(max(a))
    min_idx = a.index(min(a))
    a[max_idx] -= 1
    a[min_idx] += 1

print(max(a)-min(a))

