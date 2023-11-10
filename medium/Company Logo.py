#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    s = sorted(s)
    di = dict()

    for i in s:
        if i in di:
            di[i] += 1
        else:
            di[i] = 1

    finall = dict()
    
    for count_num in range(3):
        mv=max(di.values())
        for x,y in di.items():
            if y==mv:
                print(x,end=' ')
                print(y)
                di.pop(x)
                break
        
    
    
    
