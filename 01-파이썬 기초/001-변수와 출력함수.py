'''
변수명 정하기
  1) 영문, 숫자, _로 이루어진다.
  2) 대소문자를 구분한다.
  3) 문자나, _로 시작한다.
  4) 특수문자를 사용하면 안 된다.
  5) 키워드를 사용하면 안 된다(if, for등)
'''

a = 1
A = 2
A1 = 3
print(a, A, A1)

# 변수 선언 및 할당
a, b, c = 3, 2, 1
print(a, b, c)

# 값 교환
a, b = 10, 20
print(a, b)

a, b = b, a
print(a, b)

# 변수 타입
a = 1234554546232156542316562136548954651231231565489454652132
print(a)
print(type(a))

# 실수형은 8byte 용량까지만 가능함
a = 12.123456789123456789
print(a)
print(type(a))

a = 'student'
print(a)
print(type(a))

print()
print('=================<출력 방식>=================')

# 출력 방식
print('number')
a, b, c = 1, 2, 3
print(a, b, c)                  # 1 2 3
print('number', a, b, c)        # number 1 2 3

print(a, b, c, sep = ', ')      # 1, 2, 3
print(a, b, c, sep = '')        # 123
print(a, b, c, sep = '\n')

print(a, end = ' ')
print(b, end = ' ')
print(c)