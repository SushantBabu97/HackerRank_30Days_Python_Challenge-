# Nested Logic

"""

Task::: 
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates 
the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine=0)
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, 
fine=15 Hackos X (the number of days late).
If the book is returned after the expected return month but still within the same calendar year as the expected return date, 
the fine= 500 Hackos X (the number of days late).
If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.

Constraints:::
1<=D<=31
1<=M<=12
1<=Y<=3000

Output Format:::
Print a single integer denoting the library fine for the book received as input.

Sample Input:::
9 6 2015
6 6 2015

Sample Output:::
45

"""

Actual=str(input()).split(" ")
Da=int(Actual[0])
Ma=int(Actual[1])
Ya=int(Actual[2])

Expected=str(input()).split(" ")
De=int(Expected[0])
Me=int(Expected[1])
Ye=int(Expected[2])

fine=0

if Ya>Ye:
	fine=10000
elif Ya==Ye:
	if Ma>Me:
		fine=(Ma-Me)*500
	elif Ma==Me and Da>De:
		fine=(Da-De)*15

print(fine)