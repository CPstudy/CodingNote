def solution(arr):
    answer = []

    def square(x, y, n):
        if n == 1:
            return [1, 0] if arr[x][y] == 0 else [0, 1]

        m = n // 2
        top_left = square(x, y, m)
        top_right = square(x + m, y, m)
        bottom_left = square(x, y + m, m)
        bottom_right = square(x + m, y + m, m)

        if top_left == top_right == bottom_left == bottom_right == [0, 1] or top_left == top_right == bottom_left == bottom_right == [1, 0]:
            return top_left
        else:
            return list(map(sum, zip(top_left, top_right, bottom_left, bottom_right)))

    answer = square(0, 0, len(arr))

    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))