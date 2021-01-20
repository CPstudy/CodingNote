box = list()

def pickBlock(board, move):
    n = len(board)

    for i in range(n):
        pick = board[i][move - 1]
        if pick != 0:
            board[i][move - 1] = 0
            return pick
    
    return 0

def boomBox():
    n = len(box)

    if n >= 2:
        a = box[n - 1]
        b = box[n - 2]

        if a == b:
            box.pop()
            box.pop()
            return 2
    
    return 0

def solution(board, moves):
    answer = 0

    for move in moves:
        pick = pickBlock(board, move)
        if pick != 0:
            box.append(pick)
            answer += boomBox()

    return answer

answer = solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [1,5,3,5,1,2,1,4])
print(answer)