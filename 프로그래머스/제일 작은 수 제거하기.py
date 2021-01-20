def solution(arr):
    answer = []
    
    arr.remove(min(arr))
    answer = arr
    
    if len(arr) == 0:
        answer = [-1]
        return answer

    return answer

print(solution([4,3,2,1]))
print(solution([10]))