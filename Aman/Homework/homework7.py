
a = "The lyrics is not that poor"

notindex = a.find("not")
poorindex = a.find("poor")
print(notindex)
print(poorindex)
if notindex > 0 and poorindex >0 and poorindex > notindex:
    a = a.replace(a[notindex:(poorindex + 4)],"good")
print(a)
