t = int(input())

for i in range(t):
    n, s, e, k = map(int, input().split())
    numbers = list(map(int, input().split()))

    array = numbers[s-1:e]
    array.sort()

    print('#%d %d' %(i + 1, array[k - 1]))