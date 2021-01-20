def solution(n):
    answer = 0
    s = ''.join(sorted(str(n), reverse=True))
    answer = int(s)
    return answer

print(solution(118372))