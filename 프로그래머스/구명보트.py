def solution(people, limit):
    answer = 0

    people.sort()

    i = 0
    j = len(people) - 1

    while i <= j:
        start = people[i]
        end = people[j]
        
        answer += 1

        if start + end <= limit:
            i += 1
        j -= 1

    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))