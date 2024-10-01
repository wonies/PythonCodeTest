import sys
sys.stdin = open("07.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]


mid = n // 2
total = 0

for i in range(n):
    dist = abs(mid - i)
    start = dist
    end = n - dist
    print(f"Row {i}: start={start}, end={end}")  
    for j in range(start, end):
        print(f"i: {i}, j: {j}, each: {a[i][j]}")
        total += a[i][j]

print("Total:", total)