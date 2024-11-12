import sys
from collections import deque
sys.stdin = open("inputs/06.txt", "rt")

n, m = map(int, input().split())
a = deque(list(map(int, input().split())))
cnt = 0
while (True):
    temp = a.popleft()
    if (a and max(a) > temp):
        a.append(temp)
        if (m == 0):
            m = len(a) 
        m -= 1
    elif(a and max(a) <= temp):
        cnt += 1
        if (m == 0):
            break 
print(cnt)
