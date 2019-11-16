
number = list(range(1,101))
print(number)
squares = []
for n in number:
    s = n**2
    squares.append(s)
print(squares)
print("--------------------------------------------------------------------------------")
colors = ["red","white","blue","green","black","orange","yellow",'Aqua',"voilet","pink"]
print(colors[4])
print("------------------------------------------------------------------------")
print(colors[2:7])
print(colors[4:])
for c in colors:
    if c[0] =="b":
        print(c.upper())
    else:
        print(c)

b = int(input("Enter your age:"))

if b >= 18:
    print("you are old enought to vote")
else:
    print("Not allowed to vote")

k = int(input("Enter your age:"))

if k <=4 and k > 0:
    print("Free")
elif k < 18 and k > 4:
    print("$5 payment")
elif k >= 18 and k < 150:
    print("$10 payment")
else:
    print("inval age")
