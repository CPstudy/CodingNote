'''
변수입력과 연산자
'''

# a = input()
# print(a)

# a = input('숫자를 입력하세요: ')
# print(a)

# 여러 개 입력 받기 위해서는 split()을 쓰면 됨
# 아무 것도 없으면 띄어쓰기를 분리자로 사용함
# a, b = input('숫자를 입력하세요: ').split()
# c = a + b
# print(a, b)
# print(c)
# print(type(a), type(b), type(c))

# 숫자로 바구기
# a, b = input('숫자를 입력하세요: ').split()
# a = int(a)
# b = int(b)
# print(a + b)

# 문자를 받아서 바로 숫자로 바꾸기
# a, b = map(int, input('숫자를 입력하세요: ').split())
# print(type(a), type(b))
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)       # 몫
# print(a % b)        # 나머지
# print(a ** b)       # 거듭제곱 (2 ** 3 = 8)

# 자료형에 관해
a = 4.3
b = 5
c = a + b
print(type(c))