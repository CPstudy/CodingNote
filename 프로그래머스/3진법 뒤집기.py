def convert(n, base):
    result = ''

    while n > 0:
        if n % base < 10:
            result = str(n % base) + result
            n = n // base
        else:
            result = str(chr(55 + (n % base))) + result
            n = n // base
    
    return int(result)

def convert10(n, base):
    s = str(n)
    result = 0

    for idx, i in enumerate(s[::-1]):
        result += int(i) * (base ** idx)
    
    return result

def reverse(n):
    result = 0
    while n > 0:
        t = n % 10
        n = n // 10
        result = result * 10 + t
    
    return result

def solution(n):
    return convert10(reverse(convert(n, 3)), 3)
    

print(solution(45))
print(solution(125))