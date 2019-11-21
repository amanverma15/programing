a = input("")

def b():
    count = {}
    words = a.split(" ")
    for w in words:
        if w in count:
            count[w] = count[w] + 1
        else:
            count[w] = 1
    return count
result = b()

print(result)
