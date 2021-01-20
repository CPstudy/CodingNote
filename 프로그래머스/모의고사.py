def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c = [0, 0, 0]

    for index, a in enumerate(answers):
        x1 = p1[index % len(p1)]
        x2 = p2[index % len(p2)]
        x3 = p3[index % len(p3)]

        if a == x1:
            c[0] += 1

        if a == x2:
            c[1] += 1
        
        if a == x3:
            c[2] += 1
    
    score = max(c)

    for i in range(3):
        if score == c[i]:
            answer.append(i + 1)

    return answer

print(solution([1,2,3,4,5,2,3,4,5,1,2,3,4,5]))