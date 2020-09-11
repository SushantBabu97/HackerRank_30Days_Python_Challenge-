#Generics

"""
Write a single generic function named printArray; this function must take an array of generic elements as a parameter 
(the exception to this is C++, which takes a vector). The locked Solution class in your editor tests your function.

"""

from typing import TypeVar

Element = TypeVar("Element")


def printArray(array: [Element]):
    for element in array:
        print(element)


vInt = [1, 2, 3]
vString = ["Hello", "World"]

printArray(vInt)
printArray(vString)

"""
--------------------For C++--------------------------
#include <iostream>
#include <vector>
#include <string>

using namespace std;
template<class t>
 void printArray(vector<t> h)
{
for(t i:h)
{
cout<<i<<endl ;
}
 }

int main() {
	int n;
	
	cin >> n;
	vector<int> int_vector(n);
	for (int i = 0; i < n; i++) {
		int value;
		cin >> value;
		int_vector[i] = value;
	}
	
	cin >> n;
	vector<string> string_vector(n);
	for (int i = 0; i < n; i++) {
		string value;
		cin >> value;
		string_vector[i] = value;
	}

	printArray<int>(int_vector);
	printArray<string>(string_vector);

	return 0;
}

"""