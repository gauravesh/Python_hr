#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime,timedelta

# Complete the time_delta function below.
def time_delta(t1, t2):
    format_time="%a %d %b %Y %H:%M:%S %z"
    time1=datetime.strptime(t1,format_time)
    time2=datetime.strptime(t2,format_time)
    
    return int(abs(time1-time2).total_seconds())
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta) + '\n')


    fptr.close()
