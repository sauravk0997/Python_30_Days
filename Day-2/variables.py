#Day 2: 30 Days of python programming
import math
from cmath import pi

first_name = "Saurav"
last_name = "Kumar"
full_name = "Saurav Kumar"
country = "India"
city = "Bangalore"
age = 30
year = 2022
is_married = False
is_true = True
is_light_on = True
skills = ["Python", "Selenium", "PyTest", "SQL", "API", 18]
personal_details = {"name":"Sautav", "age":30, "city":"Bangalore"}
Games, Technology, food = "Cricket", "Python", "Briyani"
print("first name is:", first_name)
print(Games)
print(type(Games))
print(type(is_married))
print(type(city))
print(type(skills))
print(type(personal_details))
print(len(Games))
print(len(first_name))
print(len(skills))
print(len(country))
#print(len(age))
print(len(personal_details))
print(len(first_name) == len(last_name))

num_one = 5
num_two = 4
sum = num_two + num_one
print(sum)
sub = num_one - num_two
print(sub)
mul = num_two * num_one
print(mul)
div = num_one/num_two
print(div)
rem = num_one%num_two
print(rem)
exp = num_one**num_two
print(exp)
floor_division = num_one//num_two
print(floor_division)

r = 30
area_of_circle = math.pi*r**2
print(area_of_circle)
circum_of_circle = 2 * math.pi * r
print(circum_of_circle)

rad = int(input("enter radius"))
area = pi*rad**2
print(area)
first_name_a = input("Enter the name")
age_a = input("How old are you ?")
print(first_name_a)
print(age_a)
help('keywords')
help('str')