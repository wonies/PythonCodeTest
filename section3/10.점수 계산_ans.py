import sys
sys.stdin = open("11.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

sum = 0
cnt = 0

for x in a:
    if (x == 1):
        cnt += 1
        sum += cnt
    else:
        cnt = 0
        
print(sum)