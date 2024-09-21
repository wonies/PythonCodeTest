import sys
sys.stdin = open("08.txt", "rt")

n = int(input())
a = list()

def isPrime(num):  
    if (num < 2):
        return False
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

for i in range(2,n+1):
    if isPrime(i):
        a.append(i)
        
print(a)