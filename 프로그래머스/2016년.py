def solution(a, b):
    answer = ''
    weekday = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day = 0

    for i in range(a - 1):
        day += days[i]
    
    day += b
    
    answer = weekday[day % 7]

    return answer

print(solution(1, 1))