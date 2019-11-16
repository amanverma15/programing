"""Write a Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form (alphanumerically). Sample
Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red"""
a = input("Enter multiple words")

words = a.split(",")
print(words)
words.sort()
#b = sorted(words)
print(words)

print("""Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
""")
print
c = [8,2,3,-1,7]
def g(c):
     e = 0
     d = 1
     while e != 4:
         d = d * c[e]
         e = e + 1
     return d

print(g(c))


j = int
"""Write a Python function that checks whether a passed string is palindrome or not.
madam
mom
level
noon
"""
l = input('Give me a word')

def freverse(l):
    rev = ''
    for char in l:
        rev = char + rev
    return rev
r = freverse(l)
if l == r:
    print("palindrome")
else:
    print("not palindrome")
