# Enter your code here. Read input from STDIN. Print output to STDOUT
take_int=int(input())
li=[]
hash_map=dict()
for i in range(take_int):
    sample=input()
    li.append(sample)

for j in li:
    if j in hash_map:
        hash_map[j]+=1
    else:
        hash_map[j]=1
print(len(hash_map))
for i in hash_map:
    print(hash_map[i],end=' ')
