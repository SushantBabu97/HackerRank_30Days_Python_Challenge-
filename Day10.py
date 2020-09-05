# Binary Numbers

"""
Given a base-10 integer,n , convert it to binary (base-)2. 
Then find and print the base- integer denoting the 
maximum number of consecutive ‘s in ‘s binary representation.
"""


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    a=[]
    while n!=0:
    	a.append(n%2)
    	n=n//2
    
    b=''
    for i in range(len(a)):
    	b=b+str(a[i])

    b=b.split('0')
    b=map(len,b)
    print(max(b))



"""   
    print(max(map(len, bin(n)[2:].split('0'))))
 
 --bin(n) converts n to binary and returns as 0b101 for 5,
 --bin(n) strips 0b from above binary,
 --bin(n)[2:].split('0') splits the binary at 0,
 --map is done by len and max returns maximum length of it.
"""

