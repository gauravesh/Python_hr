from collections import defaultdict

n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

a_dict = defaultdict(list)
for i, el in enumerate(a, 1):
    a_dict[el].append(i)
for el in b:
    print(' '.join(map(str, a_dict[el])) if a_dict[el] else '-1')
