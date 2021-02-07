k, n = map(int, input().split())
line = []

for _ in range(k):
    line.append(int(input()))

left = 1
right = max(line)
answer = 0

while left <= right:
    mid = (left + right) // 2

    cnt = 0
    for x in line:
        cnt += x // mid
    
    if cnt >= n:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)