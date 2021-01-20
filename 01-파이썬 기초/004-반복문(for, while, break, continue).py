'''
반복문(for, while)
'''

a = range(10)       # 0부터 9까지 정수 리스트 생성
print(list(a))

a = range(1, 10)    # 1부터 9까지 정수 리스트 생성
print(list(a))

for i in range(1, 10):
    print('hello', i)

# 이렇게 하면 아무 일도 안 일어남
for i in range(10, 0):
    print('minus', i)

# 10부터 1까지 1씩 줄어듦
for i in range(10, 0, -1):
    print('minus', i)

i = 1
while i <= 10:
    print('while', i)
    i = i + 1

i = 1
while True:
    print(i)
    if i == 10:
        break
    i += 1

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# 1부터 10까지 돌다가
# 중간에 멈추게 되면
# else를 하지 않음
# 
# 정상 종료 됐을 때 else를 출력함
for i in range(1, 11):
    print(i)
    if i == 5:
        break
else:
    print(11)