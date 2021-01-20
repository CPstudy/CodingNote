def solution(n, lost, reserve):
    answer = 0
    student = [1] * n
    
    for i in reserve:
        student[i - 1] = 2

    for i in lost:
        student[i - 1] = student[i - 1] - 1
    
    for i, value in enumerate(student):
        if i > 0 and value == 0 and student[i - 1] == 2:
            student[i] = 1
            student[i - 1] = 1
        elif i < n - 1 and value == 0 and student[i + 1] == 2:
            student[i] = 1
            student[i + 1] = 1
    
    answer = n - student.count(0)

    return answer

print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))