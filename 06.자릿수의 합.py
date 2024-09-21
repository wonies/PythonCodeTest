import sys
sys.stdin = open("07.txt", "rt")
n = int(input())
# for i in range(n):
a = list(map(int, input().split()))

def digit_sum(x):
    while (x > 0):
        sum_res = x % 10
        x = x//10
    return sum_res

digit_max = -2147000000
for j in range(len(a)):
    if (digit_max < digit_sum(a[j])):
       res = a[j] 

print(res)

# n = 123
# print(n % 10)
# n //= 10
# print(n)
