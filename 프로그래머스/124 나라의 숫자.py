def solution(n):
    answer = ''
    
    while n > 0:
        r = n % 3

        if r == 0:
            r = 4

        answer = str(r) + answer
        n = n // 3

        if r == 4:
            n -= 1

    return answer

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))