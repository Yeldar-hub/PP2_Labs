x = 5
y = "Eldar"

print(x, y)

c = str(3) # "3"
v = int(3) # 3
b = float(3) # 3.0

# Legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variable names
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Multiple variables
x, y, z = "Orange", "Banana", "Apple"
print(x, y, z)

# One Value to Multiple Variables
x = y = z = "Apple"
print(x, y, z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()













