def DFS(L, sum):
    if sum > total // 2:
        return False
    if L == n:
        if sum == (total - sum):
            print("YES")
            return True
        return False
    else:
        DFS(L + 1, sum + a[L])
        DFS(L + 1, sum)
    return False
        
        

n = 6
a = [1, 3, 5, 6, 7, 10]

if __name__ == "__main__":
    total = sum(a)
    if not DFS(0, 0):  # 탐색 결과가 False면 "NO" 출력
        print("NO")