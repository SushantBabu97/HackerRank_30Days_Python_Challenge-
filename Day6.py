# Let's Review

"""
Task
Given a string, S, of length that is indexed from 0 to N-1, print its even-indexed and odd-indexed 
characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Sample Input::
2
Hacker
Rank

Sample Output::
Hce akr
Rn ak
"""

s=[]
for i in range(int(input())):
	s=input()
	print(s[::2],s[1::2])