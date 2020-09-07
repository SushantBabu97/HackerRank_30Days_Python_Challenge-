#Scope

"""
The absolute difference between two integers, a and b, is |a−b|. The maximum absolute difference 
of two integers in a set of positive integers, elements, is the largest absolute difference of any 
two integers in elements.

The class Difference is started for you in the editor. It has a private instance array (elements) 
for storing N non-negative integers, and a public integer (maxDifference) for storing the maximum 
absolute difference.

Code for handling Input/Output is provided for you in the editor. Your task is to write theclass 
constructor for Difference and the computeDifference method so that it finds themaximum absolute 
difference between any two numbers in N and stores it inmaxDifference.

Sample Input::
3
1 2 5

Sample Output::
4

"""

class Difference:
    def __init__(self, a):
        self.__elements = a
    
    # Add your code here
    def computeDifference(self):
        diff=[]
        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                absolute = abs(self.__elements[i] - self.__elements[j])
                diff.append(absolute)
        self.maximumDifference=max(diff)
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)