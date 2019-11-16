print("
3.7
.1(v3
.7
.1: 260
ec2c36a, Oct
20
2018, 14: 05:16) [MSC v.1915 32 bit(Intel)]
on
win32
Type
"help", "copyright", "credits" or "license()"
for more information.
    >> > numbers = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26,)
>> > numbers
(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26)
>> > numbers[5,]
Traceback(most
recent
call
last):
File
"<pyshell#2>", line
1, in < module >
numbers[5,]
TypeError: tuple
indices
must
be
integers or slices, not tuple
>> > numbers[5:]
(12, 14, 16, 18, 20, 22, 24, 26)
>> > numbers[4:]
(10, 12, 14, 16, 18, 20, 22, 24, 26)
>> > numbers[10:]
(22, 24, 26)
>> > numbers[9:]
(20, 22, 24, 26)
>> > numbers[1:]
(4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26)
>> > numbers[7:]
(16, 18, 20, 22, 24, 26)
>> > numbers[11:]
(24, 26)
>> > len(numbers)
13
>> > names = ("rishi", "Aman", "om", "youngates")
>> > print(names)
('rishi', 'Aman', 'om', 'youngates')
>> >
>> > combine = numbers + names
>> > print(combine)
(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 'rishi', 'Aman', 'om', 'youngates')
>> > i = numbers
>> > while i > 1
    SyntaxError: invalid
    syntax
>> > while i > 1:
    i = i + 1

Traceback(most
recent
call
last):
File
"<pyshell#23>", line
1, in < module >
while i > 1:
    TypeError: '>'
not supported
between
instances
of
'tuple' and 'int'
>> >
>> >
>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >
>> > print(names)
('rishi', 'Aman', 'om', 'youngates')
>> > numbers[4] = 50
Traceback(most
recent
call
last):
File
"<pyshell#48>", line
1, in < module >
numbers[4] = 50
TypeError: 'tuple'
object
does
not support
item
assignment
>> > numbers[4] = 50
Traceback(most
recent
call
last):
File
"<pyshell#52>", line
1, in < module >
numbers[4] = 50
TypeError: 'tuple'
object
does
not support
item
assignment
>> > del numbers[6]
Traceback(most
recent
call
last):
File
"<pyshell#53>", line
1, in < module >
del numbers[6]
TypeError: 'tuple'
object
doesn
't support item deletion
>> > {}
{}
>> > {names}
{('rishi', 'Aman', 'om', 'youngates')}
>> > {numbers}
{(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26)}
>> > phonelist = {"Rishi": 567, "Om": 234, "Aman": "younggates":678, "chad": 896}
SyntaxError: invalid
syntax
>> > phonelist = {"Rishi": 567, "Om": 234, "Aman": 987"younggates": 678, "chad": 896}
SyntaxError: invalid
syntax
>> > phonelist = {"Rishi": 567, "Om": 234, "Aman": 987, "younggates": 678, "chad": 896}
>> > phonelist.keys()
dict_keys(['Rishi', 'Om', 'Aman', 'younggates', 'chad'])
>> > phonelist.values()
dict_values([567, 234, 987, 678, 896])
>> > del phonelist["chad"]
>> > print(phonelist)
{'Rishi': 567, 'Om': 234, 'Aman': 987, 'younggates': 678}
>> > del phonelist['younggates"]

SyntaxError: EOL
while scanning string literal
>> > del phonelist["younggates"]

>> > print(phonelist)

{'Rishi': 567, 'Om': 234, 'Aman': 987}
>> > phonelist["Om"] = 999

>> > print(phonelist)

{'Rishi': 567, 'Om': 999, 'Aman': 987}
>> > sport = {'soccer': 999, 'basketball': 998, 'tennis': 997, 'football': 996, "baseball": 995}

>> > print(sport)

{'soccer': 999, 'basketball': 998, 'tennis': 997, 'football': 996, 'baseball': 995}
>> > del sport[1]

Traceback(most
recent
call
last):
File
"<pyshell#71>", line
1, in < module >
del sport[1]
KeyError: 1
>> > del sport["basketball"]

>> > print(sport)

{'soccer': 999, 'tennis': 997, 'football': 996, 'baseball': 995}
>> > del sport["tennis"]

>> > print(sport)

{'soccer': 999, 'football': 996, 'baseball': 995}
>> > sport.keys()

dict_keys(['soccer', 'football', 'baseball'])
>> > print(sport.keys)

< built - in method
keys
of
dict
object
at
0x03021570 >
>> > print(sport.keys())

dict_keys(['soccer', 'football', 'baseball'])
>> > print(sport.values())

dict_values([999, 996, 995])
>> > sport["soccer"] = 555

>> > sport["football"] = 666

>> > print(sport)

{'soccer': 555, 'football': 666, 'baseball': 995}
>> > del sport["football"]

>> > del sport["baseball"]

>> > print(sport)

{'soccer': 555}
>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> >

>> > hi = {"Om": "Soccer", "Rishi": "Read", "Aman", "Basketball", "younggates":"hike", "jack": "eating"}

SyntaxError: invalid
syntax
>> > hi = {"Om": "Soccer", "Rishi": "Read", "Aman": "Basketball", "younggates": "hike", "jack": "eating"}

          >> >

")