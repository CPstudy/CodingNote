def solution(x):
    answer = False
    number = x
    res = 0
    
    while number > 0:
        res += number % 10
        number = number // 10
    
    if x % res == 0:
        answer = True

    return answer

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))