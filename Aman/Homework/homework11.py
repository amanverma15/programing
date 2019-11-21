a = input("Enter a word:")
newstr = ""
print(a[0])
for i in range(len(a)):
    if i % 2 == 0:
        newstr = newstr + a[i]

print(newstr)
