import os
import sys
from collections import deque
#sys.stdin = open(os.path.join(sys.path[0], "in5.txt"), 'rt')

n = int(input())

words = dict()
for i in range(n):
    word = input()
    words[word] = 1

for i in range(n - 1):
    word = input()
    words[word] = 0

for key, value in words.items():
    if value == 1:
        print(key)
        break