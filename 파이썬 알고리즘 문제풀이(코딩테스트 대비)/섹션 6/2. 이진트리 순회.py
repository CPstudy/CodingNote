
# 루트 = i // 2
# 왼쪽 = i * 2
# 오른쪽 = i * 2 + 1

def dfs(v):
    if v > 7:
        return
    else:
        dfs(v * 2)
        dfs(v * 2 + 1)
        print(v, end=' ')

dfs(1)