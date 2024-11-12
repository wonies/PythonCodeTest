import sys
sys.stdin = open("05.txt", "rt")

n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))
    
meetings.sort(key=lambda x: x[1])
cnt = 0

print(meetings)

for i in range(n):
    for j in range(i, n):
        if (meetings[i][1] <= meetings[j][0]):
            cnt += 1
            i = j
            break 

print("meeting room : ", cnt)