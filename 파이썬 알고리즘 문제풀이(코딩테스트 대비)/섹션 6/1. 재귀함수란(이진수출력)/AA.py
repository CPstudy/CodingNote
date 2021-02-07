import os
import sys
sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

a = []

def binary(num):
    if num // 3 == 0:
        print(num % 3, end='')
        return
    
    binary(num // 3)
    print(num % 3, end='')

n = int(input())
binary(n)
