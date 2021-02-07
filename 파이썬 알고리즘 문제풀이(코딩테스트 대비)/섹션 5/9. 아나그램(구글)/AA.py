import os
import sys
from collections import deque
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

a = list(str(input()))
b = list(str(input()))
dict_a = dict()
# dict_b = dict()

# for x in a:
#     dict_a[x] = dict_a.get(x, 0) + 1

# for x in b:
#     dict_b[x] = dict_b.get(x, 0) + 1

# for i in dict_a.keys():
#     if i in dict_b.keys():
#         if dict_a[i] != dict_b[i]:
#             print('NO')
#             break
#     else:
#         print('NO')
        
# else:
#     print('YES')

for x in a:
    dict_a[x] = dict_a.get(x, 0) + 1

for x in b:
    dict_a[x] = dict_a.get(x, 0) - 1

for x in a:
    if dict_a.get(x) > 0:
        print('NO')
        break
else:
    print('YES')