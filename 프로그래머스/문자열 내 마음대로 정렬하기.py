def solution(strings, n):
    answer = []
    strings.sort()
    strings.sort(key=lambda s: s[n])
    answer = strings
    return answer

print(solution(['sun', 'bed', 'car'], 1))
print(solution(['abce', 'abcd', 'cdx'], 2))