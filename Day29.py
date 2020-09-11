# Bitwise AND

"""

Given set S={1,2,3,.....,N}. Find two integers, A and B (where A<B), from set S such that the value of A&B 
is the maximum possible and also less than a given integer, K. In this case, & represents the bitwise AND operator.

Sample Input:::
3
5 2
8 5
2 2

Sample Output:::
1
4
0

Explanation:::
N=5,K=2,S={1,2,3,4,5}

All possible values of A, B are:
A=1 , B=2; A&B=0
A=1 , B=3; A&B=1
A=1 , B=4; A&B=0
A=1 , B=5; A&B=1
A=2 , B=3; A&B=2
A=2 , B=4; A&B=0
A=2 , B=5; A&B=0
A=3 , B=4; A&B=0
A=3 , B=5; A&B=1
A=4 , B=5; A&B=4

The maximum possible value of A&B that is also <(K=2) is 1, so we print 1 on a new line.

"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(k-1 if ((k-1) | k) <= n else k-2)



"""

Instead of having to test various combinations of A & B, once can simply determine the result with knowledge of the 
value of the last digit of k.

Thought Process: Always strive to see if k-1 can be achieved, if not then try k-2 and so on. 
This is because the maximum value less than k is k-1, but (k-1) will only be valid if it can be formed via A&B

Here it goes:
(I) If k ends with 1, then the result is (k-1) In this case k-1 can always be formed by switching off the last digit of k, 
where k is .......1


(II) If k ends with 0, and is of form 2^m i.e. a power of 2 then result is (k-1) or (k-2). Let k=2^m If (2^{m+1})-1 is in the range, 
hen result is (k-1). In this case B=(2^{m+1})-1 and A=k-1

else, result is (k-2). (k-2) is always guaranteed as it is the precursor of a binary number that ends with a 1, see (I)


(III) The last possible case is where k ends with 0, and is not a power of 2. Again the result is either (k-1) or (k-2)

If the number obtained by switching on the rightmost 0 of (k-1) is the range, then that number can be 
bitwise multiplied by k-1 to give (k-1). Otherwise result is (k-2). (k-2) is always guaranteed as it is the precursor 
of a binary number that ends with a 1, see (I) & (II)

"""