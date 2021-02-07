import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in2.txt"), 'rt')

s = list(map(str, input()))
stack = []
answer = ''

for x in s:
    if x.isdecimal():
        answer += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and (stack[-1] != '('):
                answer += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()
        
while stack:
    answer += stack.pop()

print(answer)