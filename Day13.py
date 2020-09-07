#Abstract Class

"""
Given a Book class and a Solution class, write a MyBook class that does the following:

Inherits from Book
Has a parameterized constructor taking these parameters:
string
string
int
Implements the Book class’ abstract display() method so it prints these lines:
 a space, and then the current instance’s .
 a space, and then the current instance’s .
 a space, and then the current instance’s .

Sample Input::
The following input from stdin is handled by the locked stub code in your editor:
 The Alchemist
 Paulo Coelho
 248

Sample Output::
The following output is printed by your display() method:
 Title: The Alchemist 
 Author: Paulo Coelho 
 Price: 248

"""

from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
	def __init__(self,title, author,price):
		super().__init__(title,author)
		self.price=price
	def display(self):
		print("Title:",self.title)
		print("Author:",self.author)
		print("Price:",self.price)


title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()