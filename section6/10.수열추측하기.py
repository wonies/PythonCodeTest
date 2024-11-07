import sys
sys.stdin = open("inputs/10.txt", "rt")


def DFS(level):
    if (level == n):
        res = 0
        for i in range(n):
            res += permi[i] * combi[i]
        if (res == f):
            print(*permi)
            sys.exit(0)
    else:
        for i in range(n):
            if (ch[i] == 0):
                ch[i] = 1
                permi[level] = i + 1
                DFS(level + 1)
                ch[i] = 0


def combination(n, ord):
    return int(factorial(n) // (factorial(ord) * factorial(n-ord)))
    


def factorial(n):
    if (n==0):
        return 1
    if (n==1):
        return 1
    return n * factorial(n-1)



n, f = map(int, input().split())
print("factorial n :", factorial(n))
print("combination n : ", combination(n, 0));
combi = [0] * n
permi = [0] * n
ch = [0] * n
for i in range(n):
    combi[i] = combination(n - 1 , i)
    print("combi : ", combi[i])
res = 0
DFS(0)
print(permi)

# DFS(0)