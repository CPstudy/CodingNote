def solution(n, stages):
    answer = []
    clear = [[i + 1, 0] for i in range(n)]
    
    player = len(stages)

    for c in clear:
        if player == 0:
            c[1] = 0
        else:
            c[1] = stages.count(c[0]) / player
            player -= stages.count(c[0])
    

    clear.sort(key=lambda x: x[1], reverse=True)
    answer = [x[0] for x in clear]

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))