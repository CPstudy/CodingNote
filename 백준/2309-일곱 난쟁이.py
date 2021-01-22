n = 9
oompaloompas = []
answer = []

for _ in range(n):
    oompaloompas.append(int(input()))
    
all_weight = sum(oompaloompas)

for i in range(n - 1):
    for j in range(i + 1, n):
        weight = oompaloompas[i] + oompaloompas[j]

        if all_weight - weight == 100:
            for k in range(n):
                if k != i and k != j:
                    answer.append(oompaloompas[k])
            break
    if len(answer) == 7:
        break

answer.sort()

for oompaloompa in answer:
    print(oompaloompa, end='\n')