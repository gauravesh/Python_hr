# Enter your code here. Read input from STDIN. Print output to STDOUT

import math as m
ab = int(input())
bc = int(input())

ac = float(m.sqrt((m.pow(ab,2))+(m.pow(bc,2))))

#print(ac)
am= float((ac/2))
mc = am
#print(mc)

theta = m.asin(mc/bc)
theta = m.degrees(theta)

degree_sign = u'\N{DEGREE SIGN}'


print(round(theta),end='')
print(degree_sign)
