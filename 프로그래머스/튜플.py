import re

def solution(s):
    answer = []
    result = re.findall(r'\{([\d,]+)\}', s)
    result.sort(key=lambda k : len(k))

    tmp = set()

    for r in result:
        src = list(map(int, r.split(',')))

        for s in src:
            if s in tmp:
                continue
            else:
                tmp.add(s)
                answer.append(s)

    return answer

print(solution('{{2},{2,1},{2,1,3},{2,1,3,4}}'))
print(solution('{{1,2,3},{2,1},{1,2,4,3},{2}}'))
print(solution('{{20,111},{111}}'))
print(solution('{{123}}'))
print(solution('{{4,2,3},{3},{2,3,4,1},{2,3}}'))