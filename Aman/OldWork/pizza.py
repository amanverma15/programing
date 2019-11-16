at = ["mushroom", "chees", "peper", "olives","chicken"]
print(at)
rt = []
while True:
    k = input("What pizza toppings do you want?")
    if k == "stop":
        break
    else:
        rt.append(k)
    if k not in at:
        print("Sorry we are out of"+ k + "right now")
        break
print(rt)
