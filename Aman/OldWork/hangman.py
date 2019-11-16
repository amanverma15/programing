import random

Am = ["bob", "cool", "whatup","mathamatics","python"]
ab = random.randint(0,4)
print(Am)
An = input("Enter a word : ")

max = 5


while max != 0:
    if An == Am[ab]:
        print("You win")
        break
    elif An != Am[ab]:
        print("You lose")
        max = max - 1
        print(Am[ab])
    else:
        print("invalid input")
        print("Run again")
    An = input("Enter a word againes : ")


print("Out of loop")
