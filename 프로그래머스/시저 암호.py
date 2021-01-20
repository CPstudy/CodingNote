def solution(s, n):
    answer = ''

    for x in s:
        if x != ' ':
            if x.isupper():
                num = ord(x) + n
                num = num - 26 * ((num - ord('A')) // 26)
            else:
                num = ord(x) + n
                num = num - 26 * ((num - ord('a')) // 26)
            
            answer += chr(num)
        else:
            answer += ' '

    return answer

print(solution('AB', 1))
print(solution('z', 1))
print(solution('a B z', 4))