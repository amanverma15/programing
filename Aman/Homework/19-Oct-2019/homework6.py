#666666666666666666
a =  "fl"
m = len(a)
if m <3:
    n = a
elif a[-3:] == "ing":
    n = a + "ly"
else:
    n = a + "ing"
print(n)
