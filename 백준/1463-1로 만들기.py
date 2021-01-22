n = int(input())
answer = 0

while n > 1:
    if n == 3:
        n = n / 3
    elif n == 2:
        n = n - 1
    elif (n - 1) % 3 == 0:
        n = n - 1
    elif n % 2 == 0:
        n = n / 2
    else:
        n = n / 3
    answer += 1

print(answer)
    