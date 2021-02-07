import sys
def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())
woods = list(map(int, input().split()))

left = 1
right = max(woods)
answer = 0

while left <= right:
    mid = (left + right) // 2
    answer = 0

    for x in woods:
        r = x - mid

        if r >= 0:
            answer += r
        
    if answer >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)