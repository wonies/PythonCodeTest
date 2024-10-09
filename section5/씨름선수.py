import sys
sys.stdin = open("06.txt", "rt")

players = []

n = int(input())
for _ in range(n):
    hei, wei = map(int, input().split())
    players.append((hei, wei))
    
players.sort(key=lambda x:x[0])

print(players)

cnt = 0

for i in range(n):
    isSelected = True
    for j in range(i + 1, n):
        if (players[i][1] < players[j][1]):
            isSelected = False
            break
    if isSelected == True:
        cnt+=1 

print(cnt)