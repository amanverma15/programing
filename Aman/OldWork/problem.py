import math
'''Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9'''


a = input("GIve me a sentence: ")
uc = 0
dc = 0
for c in a:
     if c.isupper() == True:
         uc = uc +1
     if c.islower() == True:
         dc = dc + 1
print("you have " + str(dc))
print("You have " + str(uc))

print('-------------------------------------------------------------------------------------------')
'''Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.'''
for n in range(2000,3200):
    if n%7 == 0 and n%5 == 0:
        print(str(n) + ",",end =" ")
'''From sonal kukreja to Everyone:  08:47 PM
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24'''
C = 50
H = 30
v = []
r = []
D = (input("Give me a sequence of number: "))
for x in D.split(','):
    v.append(int(x))
print(v)
for x in v:
    Q  = math.sqrt((2*int(C) * int(x))/int(H))
    r.append(round(Q))

print(r)
'''Write a Python program to add 'ing' at the end of a given string
(length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged.'''

u = input("Enter a word: ")

if len(u) > 3:
    if u[-3:] == 'ing':
        u = u + 'ly'
    else:
        u = u + 'ing'
print(u)
print('-------------------------------------------------------------')
'''Write a Python program to change a given string to a new string where the first and last chars have been exchanged'''
o = input("enter a word: ")
