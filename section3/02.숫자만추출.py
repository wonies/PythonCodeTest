import sys
sys.stdin = open("inputs/02.txt", "rt")

a = input()
num = 0 
cnt = 0
for x in a:
    if (x.isdigit()):
        num = num * 10 + int(x)

for i in range(num + 1):
    if (i == 0):
        continue
    if (num % i == 0):
        cnt += 1
print(cnt)

