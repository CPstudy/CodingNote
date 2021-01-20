def solution(n):
    a = [i for i in range(1, n + 1) if n % i == 0]
    print(a)
    return sum(list(map(lambda k: k if n % k == 0 else 0, list(range(1, n + 1)))))

print(solution(12))
print(solution(5)) 