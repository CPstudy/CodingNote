import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in2.txt"), 'rt')

n = int(input())
coins = list(map(int, input().split()))
cost = int(input())
coins.sort(reverse=True)
res = 2147000000
end = False

def dfs(index, summation):
    global res
    global end
    if end:
        return
    
    
    if summation > cost:
        return
    
    if index > res:
        return
    
    if summation == cost:
        if index < res:
            res = index
    else:
        for i in range(n):
            dfs(index + 1, summation + coins[i])
        
    
dfs(0, 0)
print(res) 