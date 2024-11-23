import sys
sys.stdin = open("inputs/05.txt", "rt")

def DFS(level, divides, elements):
    global diff
    if (level == n):
        if len(set(divides)) == 3:
            temp = max(divides) - min(divides)
            print("temp: ", temp)
            diff = min(temp, diff)
        return
    for i in range(3):
        divides[i] += coinlist[level]
        DFS(level + 1, divides, elements + 1)
        divides[i] -= coinlist[level]

n = int(input())
coinlist = []
for _ in range(n):
    a = int(input())
    coinlist.append(a)
diff = 2147000000
elements = 0
divides = [0] * 3

DFS(0, divides, 0)
print("proper diff : ", diff)