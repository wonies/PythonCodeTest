import sys
sys.stdin = open("04.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
m = int(input())
k = list(map(int, input().split()))

res = a + k
res.sort()
print(res)