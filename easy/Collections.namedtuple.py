# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
head =   (input().split())
stu = namedtuple('stu',head)
sums = 0
for i in range (n):
    st = stu(*(input().split()))
    sums += int(st.MARKS)
print(sums/n)
    

