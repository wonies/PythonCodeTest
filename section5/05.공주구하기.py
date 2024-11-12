import sys
from collections import deque 

sys.stdin = open("inputs/05.txt", "rt")

n , m = map(int, input().split())
queue = deque([_ for _ in range(n)])
cnt = 0
while (len(queue) > 1):
    cnt += 1
    if (cnt == m):
        queue.popleft()
        cnt = 0
    else:
        queue.append(queue.popleft())
print(queue[0] + 1)