
def reverse(string):
    reversed_string = ""
    words = string.split()
    for i in words:
        reversed_string = " " + i + reversed_string
    print("reversed_string is: ",reversed_string)

string = input("Enter a string:")
reverse(string)





men = " Hi I am Aman and I would liketo talk to you about a string "

len(men)
