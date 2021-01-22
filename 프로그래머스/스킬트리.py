import re
def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        s = re.sub('[^%s]' %skill, '', s)
        
        for idx, x in enumerate(s):
            if x != skill[idx]:
                break
        else:
            answer += 1

    return answer

print(solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"]))