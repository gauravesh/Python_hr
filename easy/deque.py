# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

input_int=int(input())

asx=deque()


for i in range(input_int):
    isd=str(input())
    if isd == 'pop':
        asx.pop()
    elif isd == 'popleft':
        asx.popleft()
    else :
        a,b=map(str,isd.split())
        b=int(b)
        if a == 'append':
            asx.append(b)
        elif a == 'appendleft':
            asx.appendleft(b)
for i in asx:
    print(i ,end=' ')
    
