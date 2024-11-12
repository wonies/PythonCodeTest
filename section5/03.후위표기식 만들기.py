import sys
sys.stdin = open("inputs/03.txt", "rt")

a = input()

stack = []
ans = []
prior = False

print(a)

for i in range(len(a)):
    if ('0' <= a[i] <= '9'):
        ans.append(a[i])
    else:
        if (a[i] == '('):
            stack.append(a[i])
            prior = True
        elif (a[i] == ')'):
            while (stack and stack[-1] != '('):
                ans.append(stack.pop())
            stack.pop()
            prior = False
        else:
            while stack and stack[-1] not in '(' and len(stack) > 1:
                ans.append(stack.pop())
            stack.append(a[i])
while(len(stack) > 0):
    ans.append(stack.pop())
print(''.join(ans))
print(ans)
print(stack)
