import sys
sys.stdin = open("01.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

for i in range(n):
    if (m == a[i]):
        print(i+1)
        break