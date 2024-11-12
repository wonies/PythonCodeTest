import sys
sys.stdin = open("inputs/01.txt", "rt")

def find_stacks(num, m):
    stack = []
    to_remove = int(m)
    for x in num:
        while (to_remove > 0 and stack and  stack[-1] < x):
            stack.pop()
            to_remove -= 1
        stack.append(x)
    if (to_remove > 0):
        stack = stack[:-to_remove]
    return ''.join(stack)
        





n, m = input().split()
print("find the bighest number: ", find_stacks(n, m))