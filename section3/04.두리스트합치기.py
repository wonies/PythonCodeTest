import sys

sys.stdin = open("inputs/04.txt", "rt")

for _ in range(2):
    n = input()
    arr = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if (arr[i] < arr[j]):
            arr.insert(j-1, arr[i])

