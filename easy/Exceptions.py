n_tc = int(input())
a = []
b = []

for i in range(n_tc):
    ai, bi = map(str,input().split())
    a.append(ai)
    b.append(bi)

for i in range(n_tc):
    try:
        print(int(a[i])//int(b[i]))
    except Exception as e:
        print("Error Code:", e)
