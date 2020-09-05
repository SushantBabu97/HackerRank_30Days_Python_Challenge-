# Dictionaries and Maps

"""
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for. For each name queried, print the 
associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for is not found, print Not found instead.


Input::
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry


Output::
sam=99912222
Not found
harry=12299933

"""

Phonelist=dict()
n=int(input())

for i in range(n):
	name, num=input().split()
	Phonelist[name]=num

for i in range(n):
	try:
		query=input()
		if query in Phonelist:
			print(query+'='+Phonelist[query])
		else:
			print("Not found")
	except EOFError:
		break


"""
An EOFError is raised when a built-in function like input() or raw_input() do not read any data before encountering the end of their input stream. 
The file methods like read() return an empty string at the end of the file.

"""