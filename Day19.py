# Interfaces

"""
The AdvancedArithmetic interface and the method declaration for the abstract divisorSum(n) method are provided 
for you in the editor below.

Complete the implementation of Calculator class, which implements the AdvancedArithmetic interface. 
The implementation for the divisorSum(n) method must return the sum of all divisors of n.

Sample Input::
6

Sample Output::
I implemented: AdvancedArithmetic
12

"""


class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        total=0
        for i in range(1,n+1):
        	if n%i==0:
        		total=total+i
        return total
n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)