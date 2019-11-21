print("8.")

words = ["a",'of','and','then','eight']
list1 = []
for word in words:
    list1.append(len(word))
print(list1)


if list1[0] > list1[1] and list1[0] > list1[2] and list1[0] > list1[3] and list1[0] > list1[4]:
    print(words[0]+ str(" :has the logest length"))
if list1[1] > list1[0] and list1[1] > list1[2] and list1[1] > list1[3] and list1[1] > list1[4]:
    print(words[1]+ str(" :has the logest length "))
if list1[2] > list1[0] and list1[2] > list1[3] and list1[0] > list1[4] and list1[1] > list1[4]:
    print(words[2]+ str(" :has the logest length "))
if list1[3] > list1[0] and list1[3] > list1[1] and list1[3] > list1[2] and list1[3] > list1[4]:
    print(words[3]+ str(" :has the logest length "))
if list1[4] > list1[0] and list1[4] > list1[1] and list1[4] > list1[2] and list1[4] > list1[3]:
    print(words[4]+ str(" :has the logest length "))
