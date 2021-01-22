n = int(input())
m = int(input())
enable = {str(x) for x in range(10)}
if m == 0:
    pass
else:
    broken = set(input().split())
    enable = enable - broken

result = abs(n - 100)

for i in range(1000001):
    flag = True
    for x in str(i):
        if x not in enable: # 사용 불가 버튼일 경우
            flag = False
            break
    
    if flag:
        result = min(result, abs(n - i) + len(str(i)))

print(result)
