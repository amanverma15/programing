import random

az = input("Do you want to play game[Y:N]")

if az == "N":
    print("You hate this game dont you")
elif az == "Y":
    a = random.randint(1,100)
    ans = input("Enter a number : ")
    while ans.isdigit() != True
        ans = input("Enter a number : ")
        break
    b = int(ans)
    tries = 100
    q = input("press q if dont what to play the game")

    while tries != 0:
        if a > b:
            print("Too Low")
            tries = tries - 1
            b = int(input("Enter a number"))
        elif b > a:
            print("Too high")
            tries = tries - 1
            b = int(input("Enter a number"))


        elif b == a:
            print("you got the right number")
            print(a)
            print(tries)
            break
        elif b > 100:
            print("Has too be less than 100")
            b = int(input("Enter a number"))
        else:
            print("Why did your quit game")


        if tries == 0:
            break
print("Out of the loop")
