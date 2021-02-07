import math

def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        progresses[i] = math.ceil((100 - progresses[i]) / speeds[i])

        if i > 0:
            if progresses[i - 1] > progresses[i]:
                progresses[i] = progresses[i - 1]
    
    before = progresses[0]
    answer.append(1)

    for i in range(1, len(progresses)):
        if before != progresses[i]:
            before = progresses[i]
            answer.append(1)
        else:
            answer[len(answer) - 1] += 1
    
    print(progresses)

    return answer

print(solution([93, 30, 55] ,[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))