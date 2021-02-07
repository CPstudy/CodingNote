n, c = map(int, input().split())
a = []

for _ in range(n):
    a.append(int(input()))

a.sort()

left = 1
right = a[-1]
answer = 0


def count_machine(d):
    cnt = 1
    before = a[0]
    for i in range(1, n):
        if a[i] - before >= d:
            cnt += 1
            before = a[i]
    
    return cnt

while left <= right:
    mid = (left + right) // 2

    cnt = count_machine(mid)

    if cnt >= c:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
    
print(answer)