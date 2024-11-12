import sys
sys.stdin = open("03.txt", "rt")

a = [i for i in range(1, 21)]
print(a)

for _ in range(10):
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    for i in range((e - s + 1) // 2 ):
        a[s + i], a[e - i] = a[e - i], a[s + i]
        
for x in a:
    print(x, end=' ')


arr = list(20)
print(arr)