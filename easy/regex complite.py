# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def checkcompile(s):
    try:
        re.compile(s)
        return True
    except re.error:
        return False

intt=int(input())
for i in range(intt):
    st=input()
    print(checkcompile(st))
