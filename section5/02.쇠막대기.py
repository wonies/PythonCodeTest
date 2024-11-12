import sys
sys.stdin = open("inputs/02.txt", "rt")

pipe = input()
print(pipe)

stack = []
cnt = 0

for i in range(len(pipe)):
    if pipe[i] == "(":
        stack.append(pipe[i])
    elif (pipe[i] ==")"):
        stack.pop()
        if (pipe[i-1]=='('):
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)