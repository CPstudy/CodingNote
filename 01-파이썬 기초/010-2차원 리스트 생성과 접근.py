'''
2차원 리스트 생성과 접근
'''

# 10개의 0 리스트가 생김
a = [0] * 10
print(a)                 # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 3 * 3인 2차원 배열
a = [[0] * 3 for _ in range(3)]
print(a)

a[0][1] = 1
a[1][2] = 1
print(a)

for x in a:
    print(x)

for x in a:
    for y in x:
        print(y, end=' ')
    print()