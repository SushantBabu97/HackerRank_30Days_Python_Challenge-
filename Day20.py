#Sorting

"""
Given an array, a, of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm above. 
Once sorted, print the following 3 lines:

>>Array is sorted in numSwaps swaps, where numSwaps is the number of swaps that took place.
>>First Element: firstElement, where firstElement is the first element in the sorted array.
>>Last Element: lastElement, where lastElement is the last element in the sorted array.

Sample Input::
3
1 2 3

Sample Output::
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3

"""

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numSwaps=0

for i in range(n):
	for j in range(n-1):
		if a[j]>a[j+1]:
			temp=a[j]
			a[j]=a[j+1]
			a[j+1]=temp
			numSwaps+=1

print('Array is sorted in',numSwaps,'swaps.')
print('First Element:',a[0])
print('Last Element:',a[-1])

