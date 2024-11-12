import sys
sys.stdin = open("inputs/03.txt", "rt")

def DFS(level, total_time, total_price):
    global max_price
    if (total_time > n):
        return
    if (level == n):
        max_price = max(total_price, max_price)
        return
    else:
        DFS(level + times[level], total_time + times[level], total_price + price[level])
        DFS(level + 1, total_time, total_price)


max_price = -214700000
n = int(input())
times = [0] * n
price = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    times[i] = a
    price[i] = b
    
DFS(0, 0, 0)
print("max_price ", max_price)