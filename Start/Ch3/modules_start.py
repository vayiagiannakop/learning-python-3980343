# LinkedIn Learning Python course by Joe Marini
# Working with modules of code

# import the math module, which contains features for working with mathematics
# import math
# print(f"the square root of 16 is {math.sqrt(16)}")
# print(f"the value of pi is {math.pi}")
# print(f"the pow(2,10) is {math.pow(2,10)}")


# import a specific part of the module so you can refer to it more easily
# from math import pi
# print(f"the value of pi is {pi}")
# ss=[]
# import random as r
# for i in range(10):
#    print(f"A random number between 1 and 10 is {r.randint(1,10)}")
#    ss.append(r.randint(1,10))
# print(ss)
# print(f"The sum of the list is {sum(ss)}") 
   

# import a module and give it a different name


# the math module contains lots of pre-built functions


# in addition to functions, some modules contain useful constants 


# Generate a random number between 100 and 200


# try some of the math functions for yourself here:

# Use the 3rd party tabulate module to print tabulated data:

# Sample data
data = [
  ["Product", "Price", "Stock"],
  ["Laptop", 999.99, 45],
  ["Mouse", 24.99, 128],
  ["Keyboard", 59.99, 89]
]
# https://pypi.org/project/tabulate/
from tabulate import tabulate
print(tabulate(data, headers="firstrow", tablefmt="double_grid"))    


# Create a formatted table
