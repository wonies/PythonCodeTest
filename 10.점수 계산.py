import sys
sys.stdin = open("11.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
print("a", a)
cnt = 0
for i in range(n):
    if (i == 0):
        if (a[i] == 1):
            cnt += 1
    else:
        j = i
        while (j > 0):
            if (a[j] == 1):
                cnt+=1
                j-=1
            if (a[j] == 0):
                break
print(cnt)