def solution(arr):
    answer = []
    before = ''

    for i in range(0, len(arr)):
        if arr[i] != before:
            before = arr[i]
            answer.append(arr[i])

    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))