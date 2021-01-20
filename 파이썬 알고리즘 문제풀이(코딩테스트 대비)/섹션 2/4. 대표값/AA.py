import sys
# sys.stdin = open('D:/CodingNote/AA/input.txt', 'rt')

n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a) / n)
min = 2147000000

for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        # 이전 학생보다 점수가 크다면
        # 점수가 높은 학생으로 바꾸는데
        # 같은 점수라면 번호가 빠른 학생으로 해야한다.
        # 이 때 >=로 할 경우 뒷 번호로 바뀌기 때문에
        # >로 해야한다.
        if x > score:
            score = x
            res = idx + 1

print(ave, res)