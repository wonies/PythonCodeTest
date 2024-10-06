import sys
sys.stdin = open("02.txt", "rt")


n, m = map(int, input().split())
minn = 2147000000
a = list()

for i  in range(n):
    k = int(input())
    a.append(k)
    if (minn > k):
        minn = k
cnt = 0
while True:
    for i in range(n):
        cnt += a[i] // minn
    if (cnt < m // 2):
        minn = minn // 2
        cnt = 0
    else:
        cnt = 0
        for i in range(n):
            cnt += a[i] // minn
        if (cnt == m):
            break 
        else:
            minn -= 1
            cnt = 0
            
            
        
print(minn)
print(a)
