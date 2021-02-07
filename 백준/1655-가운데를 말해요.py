import heapq
import sys

n = int(sys.stdin.readline())
left = []
right = []

for _ in range(n):
    num = int(sys.stdin.readline())

    if not left:
        heapq.heappush(left, num)
    elif len(left) == len(right):
        heapq.heappush(left, num)
    else:
        heapq.heappush(right, num)
    
    heapq.heapify(left)
    heapq.heapify(right)
    
    if not left and not right and left[0] >= right[0]:
        a = heapq.heappop(left)
        b = heapq.heappop(right)
        heapq.heappush(left, b)
        heapq.heappush(right, a)
    
    print(left[0])