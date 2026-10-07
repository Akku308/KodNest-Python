# add 2 numbers
import numbers
def add():
    a, b = 10, 10
    c = a + b
    print(c)

add()
add()
add()

# find square of a numbers

def square():
    a = 5
    result = a * a
    print(result)

square()
square()
square()

# find largest of 3 numbers

def largest():
    a, b, c = 10, 25, 15

    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)

largest()
largest()
largest()

# Greet "Good morning with name"

def greet():
    name = "Akash"
    print("Good morning", name)

greet()
greet()
greet()
