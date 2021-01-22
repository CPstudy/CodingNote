n = int(input())

board = [[0] * n for _ in range(n)]
c = 0
p = 0
z = 0
y = 0
candy = ['C', 'P', 'Z', 'Y']
one = false

for i in range(n):
    board[i] = list(input())

for x in candy:
    # 행
    for i in range(n):
        for j in range(n):
            if board[i][j] == x 

print(board)