import math

print("Hello World")

#String
first_name = "Felixander"
age = 19

print(f"I am {first_name}. {age} years old")

#integer
num1 = 5
num2 = 3

print(f"If I have {num1} apples and ate {num2} of them, I have {num1 - num2} apples left.")

#float
price = 4.99
print(f"{price} is a {type(price)}")#returns what datatype it is

#boolean
status = False

if status:
    print("I'm a programmer")
else:
    print("I'm a decoder")

#typesacting
grade = 7.6
grade = int(grade)#change grade datatype into int
grade = str(grade)#change grade datatype into str

print(grade)

grade = bool(grade)#This will return True if it's not empty
print(grade)

#functions
def hello_function(name):
    print(f"Hello {name}!")

def area_rectangle(width, height):
    return width * height

def area_circle(radius):
    return math.pi * radius * radius

def area_triangle(side_a, side_b, side_c):
    return side_a * side_b * side_c

hello_function("Felixander")

first = int(area_rectangle(10, 20))
second = int(area_circle(10))
third = int(area_triangle(10, 20, 30))

print(first)
print(second)
print(third)

def greet(name):
    print("Hello", name, "!")

greet("Felix")
