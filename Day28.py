# RegEx, Patterns, and Intro to Databases


"""

Task 
Consider a database table, Emails, which has the attributes First Name and Email ID. Given n rows of data simulating the 
Emails table, print an alphabetically-ordered list of people whose email address ends in @gmail.com.

Sample Input:::
6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com

Sample Output:::
julia
julia
riya
samantha
tanya

"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    lst=[]
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if re.search(".+@gmail\.com$",emailID):
        	lst.append(firstName)
    lst.sort()
    for name in lst:
    	print(name)