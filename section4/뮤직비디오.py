import sys
sys.stdin = open("03.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

def cnt_dvd(a, capacity):
    cnt = 1
    cur = 0
    for element in a:
        if (cur + element > capacity):
            cnt += 1
            cur = element
        else:
            cur += element
    return cnt

def find_volume(a, m):
    left = max(a)
    right = sum(a)
    res = 0
    while (left <= right):
        mid = (left + right) // 2
        if (cnt_dvd(a, mid) <= m):
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res

print("volume: ", find_volume(a, m))