#Arithmetic operators
x = 15
y = 4
print(x + y) #
print(x - y) #
print(x * y) #
print(x / y) #
print(x % y) #
print(x ** y) #
print(x // y) #

print("------------------------Assignment Operators / shorthand operators-------------------------")
x = 10
print("Starting value: x =", x) #10
x = 10
print("\nAfter =  :", x) #
x += 5
print("After += 5:", x) # 
x -= 3
print("After -= 3:", x) # 
x *= 2
print("After *= 2:", x) # 
x /= 4
print("After /= 4:", x) # 
x //= 2
print("After //= 2:", x) # 
x %= 3
print("After %= 3:", x) # 0.0
x = 6
print("\nReset x =", x) # 6
x **= 2
print("After **= 2:", x) #36

print("----------Bitwise Operators----------")
x = 6
print("\nReset x =", x) #6
x &= 3                    
print("After &= 3:", x) #
x |= 2
print("After |= 2:", x) #
x ^= 5
print("After ^= 5:", x) #7
x = 4
print("\nReset x =", x) #4
x <<= 2
print("After <<= 2:", x) #16
x >>= 1
print("After >>= 1:", x) #8

print("------------Comparsion Operators/Logical Operators------------------")
x = 5
y = 3
print(x == y) #false
print(x != y) #True
print(x > y) #true
print(x < y) #false
print(x >= y) #True
print(x <= y)#False

print("------------Python allows you to chain comparison operators------")
x = 5
print(1 < x < 10) #T
print(1 < x and x < 10) #T

print("---------------------Logical Operators-------------------------")
a = True
b = False

print("a and b =", a and b) #F
print("a or b  =", a or b)#T
print("not a   =", not a)#F
print("not b   =", not b)#T

x = 10
y = 5

print("\n(x > 5) and (y < 10)  =", (x > 5) and (y < 10))#T
print("(x < 5) and (y < 10)   =", (x < 5) and (y < 10))#F

print("\n(x > 5) or (y > 10)  =", (x > 5) or (y > 10))#T
print("(x < 5) or (y > 10)    =", (x < 5) or (y > 10))#F

print("\nnot (x == 10) =", not (x == 10))#F
print("not (y == 3)   =", not (y == 3))#T

print("----------------Identity Operators------------------")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) #True
print(x is y) #False
print(x == y) #True

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y) #checks for values = true
print(x is y) #checks for pointing same object = false

print("----------------Membership operators--------------------")
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) #True

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits) #True

text = "Hello World"
print("H" in text) #True
print("hello" in text) #false
print("z" not in text) #True

print("-------------------Bitwise Operators--------------------")
a = 5
b = 3
print("a & b =", a & b) #1
print("a | b =", a | b) #7
print("a ^ b =", a ^ b) #6
print("~a =", ~a) #
print("a << 1 =", a << 1) #10
print("a >> 1 =", a >> 1) #2
