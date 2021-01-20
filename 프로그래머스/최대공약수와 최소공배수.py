def gcd(a, b):
    if a < b:
        a, b = b, a
    
    c = a % b

    if c == 0:
        return b
    
    return gcd(b, c)

def solution(n, m):
    answer = []
    answer.append(gcd(n, m))
    answer.append((n * m) // answer[0])
    return answer

print(solution(3, 12))
print(solution(2, 5))