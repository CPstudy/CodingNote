def solution(s):
    answer = ''
    low = list()
    up = list()

    for x in s:
        if x.isupper:
            up.append(x)
        else:
            low.append(x)
    
    low.sort(reverse=True)
    up.sort(reverse=True)

    answer = ''.join(low + up)

    return answer

print(solution('Zbcdefg'))