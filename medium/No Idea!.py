n, m = map(int, input().split())  # Read the values of n and m

l = map(int, input().split())  # Read the array of integers
A = set(map(int, input().split()))  # Convert A to a set of integers
B = set(map(int, input().split()))  # Convert B to a set of integers

s = 0  # Initialize the happiness counter

for i in l:
    if i in A:
        s += 1  # Increase happiness if i is in set A
    elif i in B:
        s -= 1  # Decrease happiness if i is in set B

print(s)  # Print the final happiness
