def solution(x, n):
    answer = []
    answer.append(x)
    
    for i in range(1, n):
        answer.append(answer[i - 1] + x)
    return answer

print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))