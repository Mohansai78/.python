# -*- coding: utf-8 -*-
"""day3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WFBzD4geNdK3hCSEULl65uWbfFn3lyo0

# Nestedloop: Loop inside loop is nestedloop
"""

list1=[[1,2,3],[4,5,6]]
for i in list1[0]:
    for j in list1:
        if j==2:
            break
print(j)

list1=[[1,2,3],[4,5,6]]
for i in list1[0]:
    for j in list1:
        if j==2:
            continue
print(j)

#break and continue statements only use loops while or for loop only
#pass statement it doesn't mean any changes original code when we are in the loops it helps for creating the empty function & empty clause.

d=20
print(f"for only {d:.2f} rupees")

string="for only {d:.2f} rupees"
print(string.format(d=30))

#Python string: It is a sequence which consists integers or characters

a="Hi"
print(a)

print("a")

#Property: A string is a immutable which means it cannot be changed.

a="Python programming"
print(id(a))

#[] subscript operator- It is a []bracket it is used to access the elements inside list, tuples, string etc...
#syntax
string[index]
start,stop,step

print(a)

a[7]

len(a)-1

a[17]

a[-1]

b="python"

b[-1]

b[7]

print(a)

a[0:6]#a[:6]

a[:6]

a[7:18]#a[7:]

a[7:]

a[::2]

a[-12:]

a[-12::-1]

a[::-1]

"""# Python string methods
count

"""

dir("ganesh")

a="session"
b=3

a+b

print(int.__add__(a,b))# These are magic methods(associated with classes)

a.count("s")

a.count("s",0,3)# end index is excluding

#lower
c.lower()

c="GANESH"

d="PYTHON".lower()

d

d.swapcase()

"Python".swapcase()

"the python".capitalize()

"the python".title()

"the python".upper()

"THE PYTHON".lower()

"PyThOn".upper()

#find: Built in method in string(rfind-rightfind)
x="ganesh"
x.find("e")

x="ganesh"
x.find("o")

dir(x)

"python is easy to learn and easy to understand".rfind("i")

len("python is easy to learn and easy to understand")

help("a".find("a"))

"isis".lfind("i")

#index
"isis".index("i")

help("a".index("a"))

"isis".index("n")

"isis".index(2)

a=input("enter the string: ")
b=input("enter the string: ")
if b in a:
    print(a.index(b))
else:
    print("both the substrings are different")

#strip:  3 methods:
lstrip
rstrip
strip

"""# strip

"""

a="##&python"

a.strip("#&")

a="   python   "
a.strip(" ")

a="   python   "
a.rstrip(" ")

a="   python   "
a.lstrip(" ")

date1="10-10-2023"

date1[-4:]

int(date1[-4:])

