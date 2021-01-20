import os
import sys
# sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

cards = list(range(21))

for _ in range(10):
    a, b = map(int, input().split())

    for i in range((b - a + 1) // 2):
        cards[a + i], cards[b - i] = cards[b - i], cards[a + i]

cards.pop(0)    
for x in cards:
    print(x, end=' ')