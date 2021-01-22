def print_list(x):
    for a in x:
        for b in a:
            print('%2d' %b, end=' ')
        print()

def solution(n):
    answer = []
    tmp = [[0] * n for _ in range(n)]
    direction = [(1, 0), (0, 1), (-1, -1)]
    max_number = n * (n + 1) / 2

    x = -1
    y = 0
    cnt = 0
    d = 0

    for i in range(n, 0, -1):
        for j in range(i):
            cnt += 1
            x = x + direction[d % 3][0]
            y = y + direction[d % 3][1]
            tmp[x][y] = cnt

            if x >= n:
                x = n - 1
            elif x < 0:
                x = 0

            if y >= n:
                y = n - 1
            elif y < 0:
                y = 0
        d += 1
    
    for a in tmp:
        for b in a:
            if b != 0:
                answer.append(b)
    
    return answer

print(solution(4))
print(solution(5))
print(solution(6))