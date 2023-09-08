
n = int(input())
roll_numbers_e = set(map(int, input().split()))
m = int(input())
roll_numbers_f= set(map(int, input().split()))

union_set=roll_numbers_e.union(roll_numbers_f)

print(len(union_set))
