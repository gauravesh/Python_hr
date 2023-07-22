rows,cols = map(int, input().split())


for i in range(1,rows,2):
    print((".|."*i).center(cols,"-"))
    
print("WELCOME".center(cols,"-"))

for i in range(rows-2,-1,-2):
    print((".|."*i).center(cols,"-"))
