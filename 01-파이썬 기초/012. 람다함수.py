'''
람다 함수
'''

def plus_one(x):
    return x + 1

print(plus_one(1))

plus_two = lambda x: x + 2
print(plus_two(2))

a = [1, 2, 3]

# map(function, list)
# 리스트의 요소를 함수로 처리
print(list(map(plus_one, a)))
print(list(map(lambda x: x * 2, a)))