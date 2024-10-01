import sys
sys.stdin = open("02.txt", "rt")

s = input()
num = 0

for i in s:
    if ('0' <= i <= '9'):
        num = (num * 10) + int(i)

division = 0

for i in range(num + 1):
    if (i < 1):
        continue
    if (num % i == 0):
        division+=1

print(num)
print(division)

