import os
import time

def draw_man(stage):
    one = (" ________")
    two = (" | / {}")
    three = (" |/ {}")
    four = (" | {}")
    five = (" | {}")
    six = ("___|____")

if stage == 0:
    print(one)
    print(two.format(" "))
    print(three.format(" "))
    print(four.format(" "))
    print(five.format(" "))
    print(six)



if stage == 1:
    print(one)
    print(two.format("|"))
    print(three.format(" "))
    print(four.format(" "))
    print(five.format(" "))
    print(six)


if stage == 2:
    print(one)
    print(two.format("|"))
    print(three.format("O"))
    print(four.format(" "))
    print(five.format(" "))
    print(six)



if stage == 3:
    print(one)
    print(two.format("|"))
    print(three.format("O"))
    print(four.format(" "))
    print(five.format(" "))
    print(six)



if stage == 4:
    print(one)
    print(two.format("|"))
    print(three.format("O"))
    print(four.format("--|--"))
    print(five.format("/ \\"))
    print(six)


active = True

while active:
    os.system("clear")
    current_word = raw_input("Enter a word between 3 and 10 characters:\n> ").upper()

    listed_word = list(current_word)

    blanks = "_" * len(listed_word)
    blanks_list = list(blanks)
    attempts = 4
    rounds = 0

    os.system("clear")
    draw_man(rounds)
    print(" ")
    print("You have {} lives left.".format(attempts))
    print(" ".join(blanks_list))



while attempts > 0:
    if listed_word != blanks_list:
        guess = input("Take a guess:> ")
        guess = guess.upper()

    if guess in listed_word:
    for x in range(0, len(listed_word)):
    if guess.upper() == listed_word[x]:
    blanks_list[x] = guess
    else:
    print("Nope!")
    rounds += 1
    attempts -= 1
    time.sleep(1)

    os.system("clear")
    draw_man(rounds)
    print(" ")
    print("You have {} lives left.".format(attempts))
    print(" ".join(blanks_list))

    else:
    os.system("clear")
    draw_man(rounds)
    print(" ")
    print("")
    print(" ".join(blanks_list))
    print("You got it!")
    print("You guessed it in {} attempts.".format(10 - attempts))

    play_again = raw_input("Would you like to play again? (y/n) > ")
    if play_again.lower() == "y":
    active = True
    else:
    active = False
    break

    else:
    os.system("clear")
    draw_man(rounds)
    print(" ")
    print("")
    print(" ".join(listed_word))
    print("GAME OVER. Out of guesses.")
    play_again = raw_input("Would you like to play again? (y/n) > ")
    if play_again.lower() == "y":
    active = True
    else:
    active = False

    else:
    os.system("clear")
    print("")
    print("Thanks for playing. Goodbye!")
