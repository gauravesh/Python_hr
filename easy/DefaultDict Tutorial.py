# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

A_size,B_size = map(int,input().split(' '))



a= []
for i in range(A_size):
    x=input()
    a.append(x)
    
    
b = []
for i in range(B_size):
    x=input()
    b.append(x)


new_dic = defaultdict(list)

for i in b:
    if i not in a:
        new_dic[i].append(-1)
    else:
        for index,j in enumerate(a):
            if j == i :
                new_dic[i].append(index+1)
            

            
for i in new_dic.items():
    for x in i[1]:
        print(x,end = ' ')
    print()
            

