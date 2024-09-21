import sys
sys.stdin = open("06.txt", "rt")

n,m = map(int, input().split())

a = list()
for i  in range(n + 1):
    for j in range(m + 1):
        a.append((i + 1) + (j + 1))

max_num = len(a)
cnt = [0] * (max_num + 1)
print(a)
print(cnt)

for i in a:
    cnt[i] += 1

max_cnt = max(cnt)
print("max cnt :", max_cnt)

for i, res in enumerate(cnt):
    if (res == max_cnt):
        print(i - 1, end=" ")