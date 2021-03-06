def axis(number):
    x = (number - 1) % 3
    y = (number - 1) // 3
    
    if number == 0:
        x = 1
        y = 3

    return (x, y)

def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12

    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            left = number
            answer += 'L'
        elif number == 3 or number == 6 or number == 9:
            right = number
            answer += 'R'
        else:
            la = axis(left)
            ra = axis(right)
            na = axis(number)

            ld = abs(la[0] - na[0]) + abs(la[1] - na[1])
            rd = abs(ra[0] - na[0]) + abs(ra[1] - na[1])

            if ld < rd:
                left = number
                answer += 'L'
            elif ld > rd:
                right = number
                answer += 'R'
            else:
                if hand == 'left':
                    left = number
                    answer += 'L'
                else:
                    right = number
                    answer += 'R'

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))