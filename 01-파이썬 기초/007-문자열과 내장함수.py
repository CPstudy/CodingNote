'''
문자열과 내장함수
'''

msg = 'It is Time'

print(msg.upper())         # 모두 대문자
print(msg.lower())         # 모두 소문자
print(msg)

tmp = msg.upper()
print(tmp)

# 문자열를 찾아서 index 번호를 출력함
print(tmp.find('T'))            # 1

# 인덱스 접근
print(tmp[3])                   # I

# 문자열을 찾아서 개수를 출력함
print(tmp.count('T'))           # 2

# 문자열 자르기
print(msg[:2])                  # It (0, 1)
print(msg[3:7])                 # is T (3, 4, 5, 6)

# 길이
print(len(msg))                 # 10

# 하나씩 접근
for i in range(len(msg)):
    print(msg[i], end=' ')       # I t  i s  T i m e

print()

# 문자 하나하나 접근
for x in msg:
    print(x, end=' ')            # I t  i s  T i m e
print()

# 대문자만 출력
for x in msg:
    if x.isupper():
        print(x, end=' ')        # I T
print()

# 소문자만 출력
for x in msg:
    if x.islower():
        print(x, end=' ')        # t i s i m e
print()

# 알파벳만 출력
for x in msg:
    if x.isalpha():
        print(x, end='')         # ItisTime
print()

# 아스키코드 출력
tmp = 'AZ'
for x in tmp:
    print(ord(x), end=' ')       # 65 90
print()

tmp = 'az'
for x in tmp:
    print(ord(x), end=' ')       # 97 122
print()

# 아스키코드를 문자로
tmp = 65
print(chr(tmp))                  # A