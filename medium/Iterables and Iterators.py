# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
a=int(input())
res =  ''.join(input().split())
b=int(input())
itc=(list(itertools.combinations(res, b)))
pro=0
#print(itc)
for i in itc:
    if 'a' in i:
        pro+=1
print(float(pro/len(itc)))
