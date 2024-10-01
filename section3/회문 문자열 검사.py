import sys
sys.stdin = open("01.txt", "rt")

# n = int(input())

# for i in range(n):
#     a = input().strip()
#     if (len(a) % 2 == 0):
#         matchcnt = 0
#         for j in range(len(a) / 2):
#             if (a[j] == a[j + (len(a) / 2)]):
#                 matchcnt+=1
#         if (matchcnt == (len(a) / 2)):
#             print(i, "YES")
#         else:
#             print(i, "NO")
#     else:
#         matchcnt = 0
#         for j in range((len(a) / 2) - 1):
#             if (a[j] == a[j + (len(a) / 2) - 1]):
#                 matchcnt+=1
#             if (matchcnt == (len(a) / 2)):
#                 print(i, "YES")
#             else:
#                 print(i, "NO")

n = int(input())  # Number of test cases

for i in range(n):
    a = input().strip()  # Read the string input
    
    # Check if the string is of even length
    if len(a) % 2 == 0:
        matchcnt = 0
        for j in range(len(a) // 2):  # Loop through the first half of the string
            if a[j] == a[len(a) - j - 1]:  # Compare with the corresponding character from the other half
                matchcnt += 1
        if matchcnt == len(a) // 2:  # If all characters match
            print(i + 1, "YES")
        else:
            print(i + 1, "NO")
    else:
        matchcnt = 0
        for j in range(len(a) // 2):  # Loop through the first half of the string
            if a[j] == a[len(a) - j - 1]:  # Compare with the corresponding character from the other half
                matchcnt += 1
        if matchcnt == len(a) // 2:  # If all characters except the middle one match
            print(i + 1, "YES")
        else:
            print(i + 1, "NO")
    