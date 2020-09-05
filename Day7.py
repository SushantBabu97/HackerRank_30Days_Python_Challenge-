# Array

"""
Given an array, A, of N integers, print each element in reverse order as a single line of space-separated integers.

Input::
4
1 4 3 2

Output::
2 3 4 1

"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(" ".join(map(str,arr[::-1])))

 


"""
--------------------------OR----------------------------
   print(*reversed(arr))

---------------------------------------------------------   
join() function joins the elements in a list or array.

i.e
a=['Hi','Boys','How']
"#".join(a)  >>Hi#Boys#How

""" 

