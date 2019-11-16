import time
import random



print("Hi I am a alien I am here to envade your planet but first I need some information about you goues and if dont answer I will destroy your planet. ")
print("You know when anothor planet found my planet they destroyed it without asking Question and now we are here to take your planet but before that we like some Questions. ")
myName = input(" but first, Hi what is your name")

print("Now !QUESION TIME! for " + myName)

print(myName +"(ok alien what are your questions)")
print("Are you a Rascle")

yes = input()

if yes == "yes":
   print("But you dont you dont look like me. I feel like you are lieing")
elif yes == "no":
    print("Well That explains why you dont look like me")

print("Well that was the first question which went really fast.Alright now for second Question")

print("Second Question What is your favorite song between Darkside and faded")
faded = input()
if faded == "faded":
    print("I love you")
elif faded == "darkside":
    print("I hate you")
print("Was that Second Question weird for you?YES or NO")
no = input()

if no == "yes":
    print("Well to make it clear for you its that'I love you meant the oppisite(I Hate you) and I hate you....Well you get the point.")
elif no == "no":
    print("well you are alot like us Rascle because we talk like nonsence")
print("Third Question,What do you like more Americain song or Indian song")
American = input()
if American == "Indian":
    print("You are a person I dont like you also you stink")
elif American == "American":
    print("You are a good person.")

print("I should really destroy you " + myName + " but no becuase my boss told me not to until after the 20 questions then we blow your eardrums.")

print('OK.NOW Fourth question')
print("WAIT, Until now how do you feel about yourself.good or bad")
bad = input()
if bad == "bad":
    print("I left the same when my planet was destroyed")
elif bad == "good":
    print("Weird because we will be terrified but this your planet and this planet made you different than us.")

print("What is 6565466565*53434*46547567*31232*3*6554*43253*663435**3534***34429*52532*212*34223423*52320 = is it 454355435458458437 or 58945984584353459358438 or 0,also dont write the numbers just coby it.")

fifthQuestion = input()

if fifthQuestion =="45435543545845843":
    print("You are dumb" + myName)
if fifthQuestion == " 58945984584353459358438":
    print("You are dumb" + myName)
elif fifthQuestion == "0":
    print("corect")

print("Hey " + myName + " Do you want to know why the answer is 0.yes or no")

qwertyuiop = input()

if qwertyuiop == "yes":
    print(myName + "In the fifth question the last number 52320 has a 0 and if there is a 0 in a namuber it is 0 the number is 0")
elif qwertyuiop == "no":
    print("Alright then lets move on")


wrong = input("NARRARATOR:Print that explanes that he is wrong")

print("what do you mean it is wrong if it has a 0 the answer is 0")

print(myName + ":you are so dumb")
print("Shut up " +myName + "or else I will destroy your world")

print("You known what, I am kind of angry of you and tired so I am going to take a break")


seconds = int(input("So just asking " + myName + " how many seconds do want to wait"))

for i in range(seconds):
    print(str(seconds - i) + " seconds till next episode of Question")
    time.sleep(1)

print("alright breaks over")
print("alright these questions are now going to be easy questions")


print("Sisth Question")
print("//www.netflix.com/watch/80123652?trackId=3623124&tctx=0%2C0%2C901fdfef-ec12-4bcc-8a54-823a74f441ee-4807030%2C%2C")
bald =  input("I want you to watch 3 min this video in this website and see is it(Funny,hilarios,Boring,I need to do my work) also coby the options in the left:https:")

if bald == "Funny":
    print("More like hilarios")
if bald == "Boring":
    print("You are nothing like me")
if bald == "hilarios":
    print("You are alot like me")
if bald == "I need to do my work":
    print("Go bACK in your seat")


print("Personaly from that last question it was really really really really really really really Hilarios")

print("This next question is not going to be a question it is going to be a game you are going to challege")
print("you are going to play this where to have to chose a number from 1 - 100 if you get it in less then 9 tries then you wont get killed for the next 40 year ")
print("MY friend rascle9553453454435 is going to see if you are cheating.")

amount = input("How big do you want to go in range:EXAMPLES:100, 200, 300, and so on or between it")




randomNumber = random.randrange(0,amount)
print("Random number has been generated")
guessed = False
while guessed==False:
    userInput = int(input("Your guess pleas: "))
    if userInput==randomNumber:
        guessed = True
        print("Well done!")
    elif userInput>amount:
        print("Our guess range is between 0 and 100, please try a bit lower")
    elif userInput<0:
        print("Our guess range is between 0 and 100, please try a bit higher")
    elif userInput>randomNumber:
        print("Try one more time, a bit lower")
    elif userInput < randomNumber:
        print("Try one more time, a bit higher")

print = input("Was that a good game")

if print == "bad":
    input("Why bad")
    print('You earth humans are so different from us')
if print == "good":
    print("Our kind and your kind have so much in common")




































































































































