a = int(input("Enter the first number"))
b = int(input("enter the second number"))


def add():
    sum = a + b
    print(sum)

def sub():
    sub = a - b
    print(sub)

def mul():
    mul = a * b
    print(mul)

def mod():
    mod = a%b
    print(mod)

def div():
    div= a/b
    print(div)

def expo():
    expo = a**b
    print(expo)

def floor_div():
    floor_div = a//b
    print(floor_div)

add()
sub()
mul()
mod()
div()
expo()
floor_div()

name = "Saurav Kumar"
country = "India"
str = "I am enjoying my 30 days of Python"
print(name)
print(country)
print(str)

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
list=['Saurav','Python', 'India']
print(list)
print(type(list))
dict = {'name':'Saurav','age':29,'Country':'India', 'skills':['Java','Python', 'Selenium','Testing']}
tup = (5, 'Cricket', 5.7)
set = {9, 12.5, 'Earth'}
print(set)
print(type(set))
print(tup)
print(type(tup))
print(dict)
print(type(dict))
print(type(name))
print(type(str))

import math

y2 =104
y1 = 8
x2 = 3
x1 = 2

dist = (x2 - x1)**2 + (y2-y1)**2
eluDist = math.sqrt(dist)
print(eluDist)


