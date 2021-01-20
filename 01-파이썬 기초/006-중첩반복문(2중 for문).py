'''
중첩 반복문(2중 for문)
'''

for i in range(5):
    for j in range(5):
        if j < 4 - i:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print()