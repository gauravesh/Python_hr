# Enter your code here. Read input from STDIN. Print output to STDOUT 
def diff(a_set,b_set):
    return len(a_set.difference(b_set))

a=int(input())
a_set=set(map(int,input().split()))
b=int(input())
b_set = set(map(int,input().split()))
ret=diff(a_set,b_set)
print(ret)
