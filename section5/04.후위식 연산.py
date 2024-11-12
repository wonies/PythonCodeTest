import sys
sys.stdin = open("inputs/04.txt", "rt")

op = input()
stack = []
ans = 0
for i in range(len(op)):
    x = op[i]
    if (x == '+' or x == '-' or x == '*' or x == '/'):
        if (stack):
            right = stack.pop()
            left = stack.pop()
        if (x == '+'):
            ans = left + right
            stack.append(ans)
        elif (x=='-'):
            ans = (left - right)
            stack.append(ans)
        elif (x=='*'):
            ans = (left * right)
            stack.append(ans)
        elif (x=='/'):
            ans = (left / right)
            stack.append(ans)
    else:
        stack.append(int(x))
print(stack)