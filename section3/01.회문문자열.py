# import sys
# sys.stdin = open("inputs/01.txt", "rt")

# n = int(input())
# for i in range(n):
#     a = input()
#     a= a.upper()
#     if (a == a[::-1]):
#         print("YES")
#     else:
#         print("NO")


import sys

sys.stdin = open("inputs/01.txt", "rt")

n = int(input())
for i in range(n):
    a = input()
    a = a.upper()
    alen = len(a)
    temp = 0
    for j in range((alen//2)):
        if (a[j] == a[alen - j -1]):
            temp += 1
    if  (temp == (alen // 2)):
        print("#%d YES" %(i + 1))
    else:
        print("#%d NO" %(i + 1))
