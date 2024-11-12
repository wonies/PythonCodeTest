import sys
sys.stdin = open("../inputs/01.txt")

# stack이라는 자료구조
# LIFO Last Input First Out 나중에 들어간 것이 나중에 나온다
# List 를 이용하면 됨 => list pop / append

num, m  = map(int, input().split())
num = list(map(int, str(num)))

stack = []
# for x in num:
#     while stack and m > 0

print(num)