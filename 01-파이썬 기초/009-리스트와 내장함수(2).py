'''
리스트와 내장함수(2)
'''

a = [23, 12, 36, 53, 19]

# 0부터 2까지 출력
print(a[:3])

# 1부터 3까지 출력
print(a[1:4])

# 배열 길이
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x, end=' ')
print()

for x in a:
    if x % 2 == 1:
        print(x, end=' ')
print()

# 원소와 인덱스 같이
# x는 튜플(index, value)
for x in enumerate(a):
    print(x, end=' ')
print()

# 소괄호로 열면 튜플이 됨
b = (1, 2, 3, 4, 5)
print(b)
print(b[0])

# 튜플은 값 변경이 불가능함
# b[0] = 7      # 오류

for x in enumerate(a):
    print(x[0], x[1])
print()

# enumerate를 이렇게 사용하기도 함
for index, value in enumerate(a):
    print(index, value)
print()

# a리스트를 하나씩 접근하는데
# x가 60보다 모두 작을 때 참
if all(60 > x for x in a):
    print('YES')
else:
    print('NO')

# 하나라도 참이 있으면 참
if any(60 > x for x in a):
    print('YES')
else:
    print('NO')