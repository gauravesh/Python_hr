# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(input())
a=set(map(int,input().split()))

y=int(input())
b=set(map(int,input().split()))

print(len(b.symmetric_difference(a)))
