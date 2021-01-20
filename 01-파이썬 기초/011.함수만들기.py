'''
함수 만들기
'''

# def add(a, b):
#     c = a + b
#     print(c)

# add(3, 2)
# add(5, 7)

# def add(a, b):
#     c = a + b
#     return c

# print(add(3, 2))

# 값 여러 개를 반환할 수 있음
# 튜를로 반환
# def add(a, b):
#     c = a + b
#     d = a - b
#     return c, d

# print(add(3, 2))

def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

a = [12, 13, 7, 9, 19]
for x in a:
    if isPrime(x):
        print(x, end=' ')