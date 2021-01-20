def convert(n, size):
    tmp = n
    text = ''

    while tmp > 0:
        r = tmp % 2
        tmp = tmp // 2
        text = str(r) + text
    
    for _ in range(size - len(text)):
        text = '0' + text
    
    return text

def solution(n, arr1, arr2):
    answer = []
    arr3 = [a | b for a, b in zip(arr1, arr2)]
    answer = [convert(a, n).replace('1', '#').replace('0', ' ') for a in arr3]
    

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))