import random

a = random.randint(1000,9999)

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

b = input("Enter a number from 1000 to 9999 : ")



while b != "exit":
    for i in range(a):
        cow = 0
        bull = 0
        if int(b) == i:
            cow = cow + 1
            print(cow)

        elif int(b) != i:
            bull = bull + 1
        else:
            print("Worng input")
        b = input("Enter a number from 1000 to 9999 : ")
