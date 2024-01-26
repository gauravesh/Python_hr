# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(input())
y=list(map(int,input().split()))
y.sort()
hashmap=dict()
for i in y:
    if i not in hashmap:
        hashmap[i]=1
    else:
        hashmap[i]+=1
for i in hashmap:
    if hashmap[i] == 1:
        result=i
print(result)
