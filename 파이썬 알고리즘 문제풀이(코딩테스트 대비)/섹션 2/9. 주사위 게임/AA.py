import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n = int(input())

money = list()

def score(dice):
    a, b, c = dice[0], dice[1], dice[2]

    if a == b and b == c:
        return 10000 + a * 1000
    elif a == b or a == c:
        return 1000 + a * 100
    elif b == c:
        return 1000 + b * 100
    else:
        return max(a, b, c) * 100

for i in range(n):
    dice = list(map(int, input().split()))
    cost = score(dice)
    money.append(cost)

print(max(money))