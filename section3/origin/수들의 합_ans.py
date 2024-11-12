import sys
sys.stdin = open("05.txt", "rt")

n, m = map(int, input().split())
arr = list(map(int, input().splits))

tot = arr[0]
left = 0
right = 0
cnt = 0
