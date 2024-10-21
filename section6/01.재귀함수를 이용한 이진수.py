import sys
sys.stdin = open("inputs/01.txt", "rt")

n = int(input())

def rec_binary(n):
    if (n >= 1):
        res = n % 2
        rec_binary(n // 2)
        print(res, end='')
        
rec_binary(n)