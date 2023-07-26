from collections import Counter
X = int(input())
S = Counter(map(int,input().split()))
N = int(input())
earnings = 0
for customer in range(N):
    size, price = map(int,input().split())
    if size in S and S[size] > 0:
        S[size] = S[size]-1
        earnings = earnings+price
            
print (earnings) 
