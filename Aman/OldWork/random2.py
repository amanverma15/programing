'''Write a Python program to change a given string to a new string where the first and last chars have been exchanged'''
o = input("enter a word: ")

print(o[-1] + o[1:-1] + o[0])
