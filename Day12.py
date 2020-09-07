#Inheritance

"""
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

A Student class constructor, which has 4 parameters:
A string, firstName.
A string, lastName.
An integer, id.
An integer array (or vector) of test scores, scores.
A char calculate() method that calculates a Student object’s average and returns the grade character representative of their calculated average:
Grading Scale

Sample Input::
Heraldo Memelli 8135627
2
100 80

Sample Output::
Name: Memelli, Heraldo
ID: 8135627
Grade: O

"""

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName,lastName,idNumber,testScores):
    	super().__init__(firstName,lastName,idNumber)
    	self.testScores=testScores

    def calculate(self):
    	total=0

    	for testScore in self.testScores:
    		total+=testScore

    	avg=total/len(self.testScores)

    	if 90<=avg<=100:
    		return 'O'
    	elif 80<=avg<=90:
    		return 'E'
    	elif 70<=avg<=80:
    		return 'A'
    	elif 55<=avg<=70:
    		return 'P'
    	elif 40<=avg<=55:
    		return 'D'
    	else:
    		return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())