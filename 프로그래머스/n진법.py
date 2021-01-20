def solution(n):
    answer = 0
    result = ''
    b = 16

    while n > 0:
        if n % b < 10:
            result = str(n % b) + result
            n = n // b
        else:
            result = str(chr(55 + (n % b))) + result
            n = n // b
    

    return answer

print(solution(12))
print(solution(125))