#
# 2. Write a Python program to count the number of characters (character
# frequency) in a string.
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

# from typing import List
#

def count_no_of_characters_in_string(mystr):
    dic = {}
    for c in mystr:
        if c not in dic:
            dic[c] = 1
        else:
            val = dic.get(c)
            dic[c] = val + 1
    print(dic)


if __name__ == "__main__":
    count_no_of_characters_in_string("dfskdg s.sdgs gsgh smsg")
