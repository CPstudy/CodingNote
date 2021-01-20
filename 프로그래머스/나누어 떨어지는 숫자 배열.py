def solution(arr, divisor):
    answer = []
    for x in arr:
        if x % divisor == 0:
            answer.append(x)
    
    if len(answer) == 0:
        answer = [-1]
        
    answer.sort()
    return answer

print(solution([5,9,7,10], 5))
print(solution([2,36,1,3], 1))
print(solution([3,2,6], 10))