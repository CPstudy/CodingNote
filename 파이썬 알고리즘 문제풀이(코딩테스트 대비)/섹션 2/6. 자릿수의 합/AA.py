import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n = int(input())
array = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    
    return sum

def digit_sum_by_string(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    
    return sum

max = 0

for x in array:
    if digit_sum(x) > digit_sum(max):
        max = x

print(max)