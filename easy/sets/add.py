# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
set1 = set()  # Initialize an empty set
for i in range(m):
    string = input()
    set1.add(string)

print(len(set1))
