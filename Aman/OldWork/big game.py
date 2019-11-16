import random
import time

tries = 10

while True:
    print("Hi I am Coputer and I would like you to test my ten games")
    print("Do you want to play")
    a = random.randint(1,100)
    print(a)
    b = input(" ")
    if b == "yes":
        print("Great")
        print("1st game")
        print("guessing game")
        print("rules are simple all you have to do is match the computer number from your number")
        print("You get 5 tries")
        print("I the Computer am going to give you an option that is \ngoing to make it easyer for you to play the game")
        vf = input("Do you want it : ")
        if vf == "yes":
          print("looks like you like to cheaat")
          print("You get 5 extra tries: ")
          gb = int(input("The computer has chose a number from one to hundred.\nPick a number from one to hundred. Also dont forget you have ten tries "))
          while tries >= 0:
              if gb < a:
                    print("too low")
                    tries = tries - 1
                    print("You have " + str(tries) + " left")
                    gb = int(input("Try again:Pick a number from one to hundred."))
              elif gb > a:
                    print("too high")
                    tries = tries - 1
                    print("You have " + str(tries) + " left")
                    gb = int(input("Try again:Pick a number from one to hundred."))
                else:
                    print("You win in " + str(10 - tries) + " tries")
                    print("do you want to do the game again or want move(move on) or (play again)")
                    pl = input("")
                    if pl == "move on":
                        print("alright\nnext game downloading to my system")
                        seconds = 10
                        aq = "-"
                        for i in range(seconds):
                            print(aq)
                            time.sleep(1)
                            aq = aq + '-'
                        print("Download Complete\n now we are going to play")
                    else:
                        break
              if tries == 0:
                print(" Game over you reached the limits on tries")
                print(a)
                print("do you want to do the game again or want move(move on) or (play again): ")
                kj = input("")
                if kj == "move on":
                    print("alright")
                    print("next game downloading to my system")
                    seconds = 10
                    aq = "-"
                    for i in range(seconds):
                        print(aq)
                        time.sleep(1)
                        aq = aq + '-'
                    print("Download Complete")
                    print("now we are going to play")
        elif vf == "no":
            print("arint you old fastion")
            gb = int(input("The computer has chose a number fro to hundred.\nWhat is you number?Dont forget you have five tries"))
            treis = 5
            while gb != a:
                if gb == a:
                    treis = treis - 1
                    print("you win on " + str(treis) + "tries")
                    gb = int(input("Try again:Pick a number from one to hundred."))

                elif gb < a:
                    treis = treis - 1
                    print("too low")
                    print("You have " + str(treis) + " left")
                    gb = int(input("Try again:Pick a number from one to hundred."))

                elif gb > a:
                    treis = treis - 1
                    print("too high")
                    print("You have " + str(treis) + " left")
                    gb = int(input("Try again:Pick a number from one to hundred."))
                else:
                    print("you got to pick a number from 1-100 only")
                    print("do you want to do the game again or want move(move on) or (play again)")
                    jk = input("")
                    if jk == "move on":
                        print("alright")
                        print("next game downloading to my system")
                        seconds = 10
                        aq = "-"
                        for i in range(seconds):
                            print(aq)
                            time.sleep(1)
                            aq = aq + '-'
                        print("Download Complete")
                        print("now we are going to play")

                    elif jk == "play again":
                            break
                    else:
                            print("You spelled yes and no wrong")
            if treis == 0:
                print(" Game over you reached the limits on tries")
                print("do you want to do the game again or want move(move on) or (play again): ")
                kj = input("")
                if kj == "move on":
                    print("alright")
                    print("next game downloading to my system")
                    seconds = 10
                    aq = "-"
                    for i in range(seconds):
                        print(aq)
                        time.sleep(1)
                        aq = aq + '-'
                    print("Download Complete")
                    print("now we are going to play")
    elif b == "no":
        print("You are not interested in Computer games")
    else:
        print("You print the word wrong")
        print("Since you printed the word wrong i am going to run you agian")
