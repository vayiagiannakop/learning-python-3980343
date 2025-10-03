# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
# MyList = [0, 1, 3.4, "this", False]
# print(MyList[-1])
# print (MyList[1:3]) ctrl + / to comment/uncomment
# MyList[0]=10
# print(len(MyList))
# print(MyList *2 )
# print("Vayia" * 10)
mystr="Vayia"
print(mystr[::-1])
mytuple=(1,2,3,4)   
print(mytuple)
print(mytuple[0])
print(mytuple[::-1])
myset={1,2,3,4,5,5}
print(myset)
print(3 in myset)
print(7 in myset)



      



# to access a member of a sequence type, use []


# add a list to another list


# use slices to get parts of a sequence


# you can use slices to reverse a sequence


# Tuples are like lists, but they are immutable


# Sets are also sequences, but they contain unique values

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
