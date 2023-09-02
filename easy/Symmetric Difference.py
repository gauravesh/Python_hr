# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
set_1=(input().split())

n=int(input())
set_2=(input().split)

set_1=set(list(map(int,set_1)))

set_2=set(list(map(int,set_2)))

a=set_1.difference(set_2)
b=set_2.difference(set_1)

final_set=a.union(b)
final_set=sorted(final_set)

for i  in final_set:
    print(i)

