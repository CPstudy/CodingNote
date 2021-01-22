while True:
    try:
        x = int(input())
    except EOFError:
        break

    if x == 1:
        print('1')
        continue

    answer = 0
    num = 0

    while True:
        num = num * 10 + 1
        answer += 1
        if num % x == 0:
            print(answer)
            break