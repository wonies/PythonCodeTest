import sys
sys.stdin = open("09.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
literal = []
cnt = 0
last = 0
while (a):
    if (a[0] > last and a[-1] > last):
        if (a[0] > a[-1]):
            literal.append("R")
            last = a[-1]
            a.pop(-1)
        else:
            literal.append("L")
            last = a[0]
            a.pop(0)
    elif (a[0] > last):
        literal.append("L")
        last = a[0]
        a.pop(0)
    elif (a[-1] > last):
        literal.append("R")
        last = a[-1]
        a.pop(-1)
    else:
        break
    cnt+=1  

print(cnt)

print("literal : ", literal)

