# Enter your code here. Read input from STDIN. Print output to STDOUT

a=int(input())
spli = set(map(int,input().split()))
b=int(input())
splj=set(map(int,input().split()))
print(len(spli.intersection(splj)))
