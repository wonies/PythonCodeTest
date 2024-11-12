import sys
sys.stdin = open("inputs/03.txt", "rt")

a = [i for i in range(1, 21)]
print(a)

for _ in range(10):
    n, m = map(int, input().split())
    a[n-1:m]= a[n-1:m][::-1]

print(a)

# 두번째 문제풀이

# for _ in range(10):
#     n, m = map(int, input().split())
#     left, right = n - 1, m - 1
#     while (left <= right):
#         a[left] , a[right] =  a[right], a[left]
#         left += 1
#         right -= 1
        
# print(a)