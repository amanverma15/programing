"""Write a Python function that takes a list and returns a new list with unique elements of the first list.
"""
list1 = ['a','b','c','d','e','a','b','a','b','d','f']

def unqie(list2):
    list3 = []
    for i in list2:
        if i in list3:
            continue
        else:
            list3.append(i)
    return list3
unqielist = unqie(list1)
print(unqielist)


