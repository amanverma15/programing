
def merge_convert(a, b):
    if len(a) < 2 and len(b) < 2:
        return "Invalid input"
    c = b[0:2] + a[2:] + ' ' + a[0:2] + b[2:]
    return c

if __name__ == "__main__":
    a = input("Enter first string : ")
    b = input ("Enter second string : ")
    print(merge_convert(a, b))
