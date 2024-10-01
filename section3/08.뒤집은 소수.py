import sys
sys.stdin = open("09.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

def reverse(x):
    res = 0 
    while (x > 0):
        temp = x % 10
        res = (res * 10) + temp
        x //= 10
    return res

def isPrime(num):
    if (num < 2):
        return False
    for i in range(2, num//2+1):
        if (num % i == 0):
            return False
    return True

result = list()

for i  in range(n):
    prime = reverse(a[i])
    if (isPrime(prime)):
        result.append(prime)

print(result)
        