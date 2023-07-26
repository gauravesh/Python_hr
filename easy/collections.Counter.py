

# Number of shoes
X = int(input())
shoe_list = list(map(int, input().split()))

# Number of customers
N = int(input())
num_arr, price_arr = [], []
for _ in range(N):
    num, price = map(int, input().split())
    num_arr.append(num)
    price_arr.append(price)

total_price = 0
for number, shoe in enumerate(num_arr):
    if shoe in shoe_list:
        total_price += price_arr[number]
        shoe_list.remove(shoe)  # Remove the shoe size from the list to prevent double-selling

print(total_price)
