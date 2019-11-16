Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> list1 = ['f', 'dfdf', 4, 5, 2223]
>>> print(list1)
['f', 'dfdf', 4, 5, 2223]
>>> list1[3] = 'ram'
>>> print(list1)
['f', 'dfdf', 4, 'ram', 2223]
>>> list1.remove(4)
>>> print(list1)
['f', 'dfdf', 'ram', 2223]
>>> del list1[4]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    del list1[4]
IndexError: list assignment index out of range
>>> del list1[1]
>>> print(list1)
['f', 'ram', 2223]
>>> 
>>> list2 = ["fs", 345, "t"]
>>> list = list1 + list2
>>> print(list)
['f', 'ram', 2223, 'fs', 345, 't']
>>> 
>>> list
['f', 'ram', 2223, 'fs', 345, 't']
>>> 
