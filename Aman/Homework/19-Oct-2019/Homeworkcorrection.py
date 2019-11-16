print("1")
hard = input('Please Enter a string: ')
print(len(hard))
print('------------------------------------------------------')
print("2")
string2 = input("Enter a string")
print("string = words")
count = {}
for char in string2:
    keys = count.keys()
    if char in keys:
        count[char] += 1
    else:
        count[char] = 1
print(count)
print("-------- - --- - - - -- - ")
print("dictionary example")
student = {'name':"Aman",'age':13,"hobby":"playing","country":"Claifornia"}
#A dictionary is a collection which is unordered, changeable and indexed.
#In Python dictionaries are written with curly brackets, and they have keys
# and values.
print(student)
print(student.keys())
print(student.values())



#'do 3rd and 6th"







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
