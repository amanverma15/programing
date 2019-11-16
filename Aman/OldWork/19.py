op1 = 0.0
op2 = 0.0
op = ""
a = int(input("how many times you want to use the calator"))
b = 1
while op1 != 'q' and a > b :
    print("Enter the first number(q to quit)::: ")
    op1 = input()
    if op1 == "q":
        break
    b = b + 1
    if a == b:
        break
    op1 = float(op1)
    op2 = float(input("Enter the second number ::: "))
    op = input("Chose an operation(+, -, *, /)")
    if op == "+":
        print(op1 + op2)
    elif op == "-":
        print(op1 - op2)
    elif op == "*":
        print(op1 * op2)
    elif op == "/":
        print(op1/op2)
    else:
        print("Invalid input")

print("out of the loop")


t = 0
answer = 'Whatson'
while t <= 3:
    r = input("What is the name of computer played on Jeopardy?")
    t = t + 1
    if r == "Whatson":
        print("Correct answer")
        break
    elif t == 3:
        print("Answer is Whatson")
        break
    else:
        print("Sorry, Try Again")


import random

r = random.randint(1,6)
s = input("Do you want to play dice")
if s == "y" or "yes":
    u = int(input("Enter number"))
    if u != r:
        print("incorrect number")
    if u == r:
        print("Rolled correct number")
if s == "n":
    break
