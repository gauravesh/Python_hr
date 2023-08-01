from itertools import combinations

string, k = input().split()
for y in range(1, int(k) + 1):
    for x in sorted(list(combinations(sorted(string), y))):
        print("".join(x))
