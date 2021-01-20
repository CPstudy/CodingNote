def solution(s):
    answer = ''
    cnt = 0

    for x in s:
        if cnt % 2 == 0:
            answer += x.upper()
        else:
            answer += x.lower()
        
        cnt += 1
        
        if x == ' ':
            cnt = 0
    return answer

print(solution('try hello world'))