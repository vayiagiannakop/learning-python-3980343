# LinkedIn Learning Python course by Joe Marini
# Example file for working with Exceptions
#

# Errors can happen in programs, and we need a clean way to handle them
# This code will cause an error because you can't divide by zero:

# Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
# try:
#   x=10/0
# except:
#   print("You can't divide by zero!")
# 
# Python code​​​​​​‌‌‌​​‌​‌​​‌‌‌‌​​‌​‌‌‌​​​‌ below
# Use print("messages...") to debug your solution.

def is_palindrome(teststr):
    # Your code goes here.
    teststr = teststr.strip()
    teststr = teststr.upper()
    teststr = teststr.replace(" ", "").replace("!", "").replace(",", "")
    teststr = teststr.replace(".", "")
    teststr = teststr.replace("?", "").replace(";", "").replace(":", "")
    teststr = teststr.replace("-", "") 
    teststr = teststr.replace("_", "").replace("@", "")
    teststr = teststr.replace("#", "").replace("$", "")
    teststr = teststr.replace("'", "").replace("^", "")
    teststr = teststr.replace("&", "")    
    teststr = teststr.replace(" ", "").replace("!", "")
    teststr = teststr.replace(",", "").replace(".", "")
    if teststr == teststr[::-1]:
      return True
    else:
      return False
    if teststr == teststr[::-1]:
      return True
    else:
       return False
    
print(is_palindrome("Hello !! "))
print(is_palindrome("A   !!??d  a"))

  

# You can also catch specific exceptions

