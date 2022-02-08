from math import pi

print("age", 30)
print("Height:", 5.6 )
comp = 5+6j
print(comp)
print(type(comp))

base = int(input("Enter the base of triangle"))
height = int(input("Enter the height of triangle"))
area_triangle = 0.5*base*height
print(area_triangle)

a =int(input("Enter side a"))
b =int(input("Enter side b"))
c =int(input("Enter side c"))
perimeter_of_triangle = a+b+c
print("Perimeter of triangle is : ",perimeter_of_triangle)

length = int(input("Enter the length"))
breadth = int(input("Enter the breadth"))
area = length*breadth
perimeter_of_rect = 2*(length+breadth)
print("Area of rect: ",area)
print("perimeter of rectangle : ", perimeter_of_rect)

radius = int(input("Enter the radius"))
area_circle = pi*radius*radius
print("area of circle is : ",area_circle )
perimeter_circle = 2*pi*radius
print("perimeter of circle is : ", perimeter_circle)

x = int(input("Enter the x value"))
y = 2*x-2
print("The value of Y is : ",y)
y2 = int(input("Enter the y2 value "))
y1 = int(input("Enter the y1 value "))
x2 = int(input("Enter the x2 value "))
x1 = int(input("Enter the x1 value "))
m = (y2-y1)/(x2-x1)
print(m == y)
print("The value of m is: ",m)
x3 = int(input("Enter x3 values"))
y3 = (x3**2)+(6*x3)+9
print(y3)
print(len("Python") != len("Dragon"))
print('on' in 'python')
print('on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon.')
print('on' not in 'python')
print('of' not in 'dragon')
a1 = len('python')
print(a1)
print(type(a1))
b1 = float(a1)
print(b1)
print(type(b1))
c1 = str(b1)
print(c1)
print(type(c1))

n = int(input("Enter any number : "))
if n%2 == 0 :
    print("number is even")
else:
    print("number is odd")

fl_div = 7//3
print(fl_div)
print(fl_div == 2.7)
print(type('10') == type(10))
print(int(9.8) == 10)
