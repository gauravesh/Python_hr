# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
n,m=map(int,input().split())
lis=list()
for i in range(n):
    temp=list(map(int,input().split()))
    lis.append(temp)
numpy_list=np.array(lis)
print(np.transpose(numpy_list))
print(numpy_list.flatten())
