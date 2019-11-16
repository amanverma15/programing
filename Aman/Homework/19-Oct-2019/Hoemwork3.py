import sys

def fl(b):
    if len(b) > 1:
        c = b[0:2]
        d = b[-2:]
        n = c + d
        return n
    else:
        return "Empty String"

def main(argv):
    if len(sys.argv) > 1 and len(sys.argv) < 3:
        print(fl(sys.argv[1]))
    else:
        print("Too many argunments")

if __name__ == "__main__":
   main(sys.argv[1:])

"""Write a Python program that accepts a hyphen-separated
sequence of words as input and prints the words in a hyphen-separated
sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow"""

a = input("Enter 5 words")
words = a.split("-")
print(words)
words.sort()
print('-'.join(words))
