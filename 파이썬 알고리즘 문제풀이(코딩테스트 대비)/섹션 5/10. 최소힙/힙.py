n = 9
heap = [7, 6, 5, 8, 3, 5, 9, 1, 6]

for i in range(1, n):
    c = i
    while True:
        root = (c - 1) // 2
        if heap[root] < heap[c]:
            heap[root], heap[c] = heap[c], heap[root]
        c = root
        if c == 0:
            break

print(heap)