e, s, m = map(int, input().split())
ee, ss, mm = 1, 1, 1
maxe, maxs, maxm = 15, 28, 19

y = 1
while True:
    if e == ee and s == ss and m == mm:
        print(y)
        break

    y += 1
    ee += 1
    ss += 1
    mm += 1

    if ee > maxe:
        ee = 1
    
    if ss > maxs:
        ss = 1
    
    if mm > maxm:
        mm = 1
