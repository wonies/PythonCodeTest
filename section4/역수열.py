import sys
sys.stdin = open("10.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
origin = [0] * (n)

for i in range(n):
    cnt = a[i]
    for j in range(n):
        if (origin[j] == 0):
            if (cnt == 0):
                origin[j] = i + 1
                break 
            else:
                cnt -= 1
                
                
print(' '.join(map(str, origin)))