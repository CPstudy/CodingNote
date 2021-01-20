import re
def solution(dartResult):
    mat = re.findall(r'\d+[A-Z][\*\#]?', dartResult)

    a = [0] * 3

    for index, m in enumerate(mat):
        t = re.match(r'(\d+)([A-Z])([\*\#]?)', m)
        score = int(t.group(1))
        bonus = t.group(2)
        option = t.group(3)

        sqt = 1
        opt = 1

        if bonus == 'D':
            sqt = 2
        elif bonus == 'T':
            sqt = 3
        
        if option == '*':
            opt = 2

            if index > 0:
                a[index - 1] *= 2
            
            a[index] *= 2
        
        elif option == '#':
            opt = -1
        
        a[index] = (score ** sqt) * opt

    return sum(a)

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))