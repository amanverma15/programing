"""A school with 600 students wants to produce some information
from the results of the four standard tests in Maths, Science,
 English and IT. Each test is out of 100 marks. The information
 output should be the highest, lowest and average mark for each
 test and the highest, lowest and average mark overall. All the
 marks need to be input. Write a program to complete this task."""
m = []
s = []
it = []
e = []
a = 0
while a != 3:
    mm = int(input("ENTER a STUDENTS GRADE IN MATHS:  "))

    m.append(mm)
    sm = int(input("ENTER A STUDENTS GRADE IN Science:  "))
    s.append(sm)
    em = int(input("ENTER A STUDENTS GRADE IN English:  "))
    e.append(em)
    itm = int(input("ENTER A STUDENTS GRADE IN it:  "))
    it.append(itm)
mh =  max(m)
sh = max(s)
eh = max(e)
ith = max(it)
ml =  min(m)
sl = min(s)
el = min(e)
itl = min(it)
print(mh,sh,eh,ith,ml,sl,el,itl)
