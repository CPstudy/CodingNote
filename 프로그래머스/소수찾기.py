def solution(n):
    answer = 0
    ch = [False] * (n + 1)

    for i in range(2, n + 1):
        if ch[i] == False:
            answer += 1
            for j in range(i, n + 1, i):
                ch[j] = True

    return answer

print(solution(10))