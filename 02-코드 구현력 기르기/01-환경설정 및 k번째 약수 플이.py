a, b = map(int, input().split())
count = 0

for i in range(1, a + 1):
    if a % 6 == 0:
        count += 1
        if count == b:
            print(i)
            break
else:
    print(-1)