#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    s=sorted(s)
    di=dict()
    for i in s:
        if i in di:
            di[i]+=1
        else:
            di[i]=1
    finall=dict()
    
    while len(finall)<3 :
        one=max(di.values())
        popper=''
        for x,y in di.items():
            if y == one:
                popper=x
                finall[x]=y
        di.pop(popper)

    for x,y in finall.items():
        print(x,end=' ')
        print(y)
    
        
    
