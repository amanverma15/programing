"""Check whether the password is valid or not with the help of few conditions.

Conditions for a valid password are:

Should have at least one number.
Should have at least one uppercase and one lowercase character.
Should have at least one special symbol.
Should be between 6 to 20 characters long."""
a = input(" Please enter your Password: ")
s = ["!","%",'^','^','*','@']
while len(a) < 6 and len(a) > 20:
    print("lenth of the password must be greater than 6 and less than 20")
    a = input(" Please enter your Password: ")
while not any(char.isdigit()for char in a):
    print("Password should have atleast 1 number")
    a = input(" Please enter your Password: ")
while not any(char.isupper()for char in a):
    print("password should contain one upper case")
    a = input(" Please enter your Password: ")
while not any(char.islower()for char in a):
    print("password should contain one lower case")
    a = input(" Please enter your Password: ")
while not any(char in s for char in a):
    print("password should contain one symbol case")
    a = input(" Please enter your Password: ")
print("--------------------------------------------------------------------------------------")
'''Write a Python program to calculate a dog's age in dog's years.
Expected Output:
15 human years equals the first year of a medium-sized dog’s life.
Year two for a dog equals about nine years for a human.
And after that, each human year would be approximately five years for a dog.'''

human = int(input("Enter dog age in humun years"))

if human == 1:
    dog = 15
if human == 2:
    dog = 15 + 9
if  human > 2:
    dog = 15 + 9 + ((human -2)*5)
print(dog)
'''5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 4'''
h = int(input("give me a number"))
x = 0
while x != 9:
    print(str(h) + " x " + str(x) + " = " + (str(h*x)))
    x = x + 1
