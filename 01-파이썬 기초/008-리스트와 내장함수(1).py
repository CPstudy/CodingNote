'''
리스트와 내장함수(1)
'''

import random as r

# 빈 리스트
a = []
b = list()
print(a)
print(b)

# 리스트 초기화
a = [1, 2, 3, 4, 5]
print(a)
print(a[0])

b = list(range(1, 11))
print(b)

# 리스트 합치기
c = a + b
print(c)

# 값 추가
print(a)
a.append(6)
print(a)

# 특정 인덱스에 값 추가
a.insert(3, 7)
print(a)

# 맨 마지막에서 값을 꺼내고 제거
a.pop()
print(a)

# 특정 인덱스에서 값을 꺼내고 제거
a.pop(3)
print(a)

# 특정 값을 제거
a.remove(4)
print(a)

# 특정 값을 찾아서 인덱스 반환
print(a.index(5))

print('=========================')
a = list(range(1, 11))
print(a)

# 리스트의 합
print(sum(a))

# 리스트의 최댓값, 최솟값
print(max(a))
print(min(a))

# 섞기
r.shuffle(a)
print(a)

# 오름차순 정렬
a.sort()
print(a)

# 내림차순 정렬
a.sort(reverse=True)
print(a)

# 리스트 비우기
a.clear()
print(a)

a = [int(c) + 1 for c in str(123)]
print(a)