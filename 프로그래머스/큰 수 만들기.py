def solution(number, k):
    answer = ''
    a = []
    last = 0
    for idx, x in enumerate(number):

        while a and a[-1] < x and k > 0:
            a.pop()
            k -= 1
        
        if k == 0:
            a += number[idx:]
            break
        
        a.append(x)
    
    a = a[:-k] if k > 0 else a
    answer = ''.join(a)

    return answer

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("777766", 2))
print(solution("667777", 2))