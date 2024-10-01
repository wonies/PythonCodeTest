import sys
sys.stdin = open("06.txt", "rt")


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

maxvalue = -2147000000
temp = -2147000000
slash = 0
revslash = 0

for i in range(n):
    val1 = val2 = 0
    for j in range(n):
        if (i == j):
            slash += a[i][j]
        if (i + j == n -1):
            revslash += a[i][j]
        val1 += a[i][j]
        val2 += a[j][i]
    if (maxvalue < val1):
        maxvalue = val1
    elif (maxvalue < val2):
        maxvalue = val2
    elif (maxvalue < slash):
        maxvalue = slash
    else:
        maxvalue = revslash
    
print(maxvalue)