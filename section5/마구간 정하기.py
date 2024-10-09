import sys
sys.stdin = open("04.txt", "rt")

n, c = map(int, input().split())
a = [int(input()) for _ in range(n)]


def cnt_horse(a, mid):
    cnt = 1
    pos = a[0]
    for i in range(1, len(a)):
        if  (a[i] - pos >= mid):
            cnt += 1
            pos = a[i]
    return cnt


def find_stalls(c, a):
    a.sort()
    left = 1
    right = a[-1] - a[0]
    res = 0
    while (left <= right):
        mid = (left + right) // 2
        if (cnt_horse(a, mid) >= c):
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res


    
print("res : ", find_stalls(c, a))