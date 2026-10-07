# Arguments - Input and Return value - Output
# No arguments + No return value 
def square1():
    num = 3
    square = num * num
    print(square)

square1()

# No arguments + Return value
def square2():
    num = 5
    square = num * num 
    return square 
res = square2()
print(res)

# Arguments + No return value 
def square3(num):
    square = num * num
    print(square)
square3(10)

# Arguments + Return value
def square4(n): # parameters 
    sqr = n * n 
    return sqr
print(square4(1))# arguments

# return statement 
def calculate(a, b):
    sum = a + b
    diff = a - b
    return sum, diff

sumres, diffres = calculate(10, 6)
print(sumres)
print(diffres)
