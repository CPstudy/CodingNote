n = int(input())
meetings = []

for _ in range(n):
    a, b = map(int, input().split())
    meetings.append((a, b))

meetings.sort(key=lambda x: x[0])
meetings.sort(key=lambda x: x[1])

end = meetings[0][1]
count = 1

for i in range(1, n):
    if meetings[i][0] >= end:
        end = meetings[i][1]
        count += 1

print(count)