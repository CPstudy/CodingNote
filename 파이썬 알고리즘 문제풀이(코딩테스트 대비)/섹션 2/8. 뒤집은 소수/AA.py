import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n = int(input())
array = list(map(int, input().split()))

def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        x = x // 10
        res = res * 10 + t
    
    return int(res)

def isPrime(x):
    if x == 1:
        return False

    for i in range(2, x // 2):
        if x % i == 0:
            return False
    
    return True


for x in array:
    if isPrime(reverse(x)):
        print(reverse(x), end=' ')