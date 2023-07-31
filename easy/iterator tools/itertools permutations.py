# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations
inp = input()
parts = inp.split()
t_parts = parts[0]
n_parts = int(parts[1])
a_list = (list(permutations(t_parts,n_parts)))
a_list.sort()

for element in a_list:
    print(''.join(element))
    
