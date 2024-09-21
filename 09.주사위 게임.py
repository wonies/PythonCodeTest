import sys
sys.stdin = open("10.txt",  "rt")

n = int(input())
res = 0

for i in range(n):
    t1, t2, t3 = map(int, input().split())
    if (t1 == t2 & t2 == t3 & t1 == t3):
        temp = 10000 + (t1 * 1000)
    elif (t1 == t2 | t2 == t3):
        temp = 1000 + (t2 * 100)
    elif (t1 == t3 | t2 == t3):
        temp = 1000 + (t3 * 100)
    elif (t1 == t2 | t1 == t3):
        temp = 1000 + (t1 * 100)
    else:
       ts = max(t1, t2, t3)
       temp = ts * 100
    if (temp > res):
        res = temp
        
print(res)