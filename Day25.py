#Running Time and Complexity

"""
A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
Given a number, n, determine and print whether it's Prime or Not prime.
If possible, try to come up with a O(sqrt(n)) primality algorithm, or see what sort of optimizations you come up with for an O(n) algorithm. 

Sample Input:::
3
12
5
7

Sample Output:::
Not prime
Prime
Prime

"""

from math import *

n=int(input())

def isPrime(a):
	for i in range(2,int(ceil(sqrt(a)))):
		if a%i==0:
			return False
	return True

for j in range(n):
	a=int(input())
	if a>=2 and isPrime(a):
		print("Prime")
	else:
		print("Not prime")

