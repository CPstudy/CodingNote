import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n, m = map(int, input().split())
boats = list(map(int, input().split()))

boats.sort(reverse=True)
answer = 0

s = 0
e = n - 1

while s <= e:
    first = boats[s]
    second = boats[e]
    
    if first + second > m:  # 몸무게가 m의 반보다 무거우면 그냥 혼자 보냄
        s += 1
        answer += 1
    else:   # 그게 아니라면 가장 가벼운애랑 같이 보냄
        s += 1
        e -= 1
        answer += 1

print(answer)
