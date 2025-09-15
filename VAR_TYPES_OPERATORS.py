# # Python Basics
#
# # Variables
#
# # Assigning values to variable
# x = 10 # an integer
# name = "Liam" # a string
# is_happy = True # a boolean
#
# ## Using variables
# print(x)
# print("Hello", name)
# print("Are you happy", is_happy)
#
# # Reassigning Values
# x = 20
# print("Now x is:", x)
#
# # Memory Concept
# my_number = 5
# print(my_number) # 5
#
# my_number = my_number + 3
# print(my_number) # 8
#
# favourite_food = "Pie & Mash"
# birth_year = 1964
#
# print("I was born in ", birth_year)
# print("My favorite food is", favourite_food)
#
# print("I was born in ", birth_year, "and my favourite food is ", favourite_food,".")
#
# # Primitive Types
# # int -->. whole numbers (1, 47, -10)
# # float --> (3.14, 0.5, -2.0)
# # str --> text data ("hello", "world", "my name is")
# # bool --> logical values (True, False)
#
# # Types Code-along
# import sys # allows us to check the memory size of an object
#
# # integer
# num_1 = 1
# print(num_1)
# print(type(num_1)) # <class 'int>
# print(sys.getsizeof(num_1))  # 28 bytes
#
# # #float
#
# float_1 = 1.0
# print(float_1) # <class "float">
# print(type(float_1)) # 24
# print(sys.getsizeof(float_1))
#
# # string
# str_1 = "1"
# print(str_1)
# print(type(str_1))  # < class 'str'>
# print(sys.getsizeof(str_1)) # bytes 42
#
# # Boolean
# bool_1 = True #must be capitalised
# print(bool_1)
# print(type(bool_1)) # <class "bool">
# print(sys.getsizeof(bool_1)) # 28 bytes
#
# days = 7 # number of days
# print(days) #print days
# print(type(days))   #class "int">
# print(sys.getsizeof(days)) # 28 bytes
#
# price = 20.40 #float value in decimal
# print(price) # price value
# print(type(price)) # <class "float">
# print(sys.getsizeof(price)) # 24 bytes
#
# name = "Liam" #string
# print(name) #print string
# print(type(name))  # <class 'str'>
# print(sys.getsizeof(name)) #  45 bytes
#
# raining = True # boolean
# print(raining)  # PRINT VARIABLE
# print(type(raining)) # <class 'bool'>
# print(sys.getsizeof(raining)) # 28 bytes
#
# print("-------------------------------------")
# print(raining, type(raining), sys.getsizeof(raining))
#
# # Casting
#
# # Casting means changing on type to another
# # You can convert from one compatible type  (int --> float, bool --> int
# # You can't convert directly incompatible type ( "hello" --> int)
#
# # Casting examples
# my_num = 5
# my_float = float(my_num) # 5.0
# print(my_float)
#
# my_str = "123"
# my_int = int(my_str) #  works if string is numeric
# print(my_int)
#
# # my_bad_str = "Hello"
# # my_bad_int = int(my_bad_str) #incompatible types
# # print(my_bad_int)
#
# print(int(False)) # 0
# print(int(True)) # 1

# User Input
# my_num_input = int(input("Enter a number: ")) # input will be str by default
# print(type(my_num_input))
#
# user_age = int(input("What is your age? >> "))
# print("You are ", user_age, "years old.")
#
# cast_num = float(input("Pls enter a decimal number:  "))
# float_num = (float(cast_num))
# print(float_num)

# arithmetic and comparison operators

# Python uses standard mathematical operators:
# + addition
# - subtraction
# * multiplication
# / division --> returns a float
# % modulo --> returns a remainder

# Comparison operators
# > (grt than)
# < (less than)
# >= (gtr than or equal to)
# <= (less than equal to)
# == (equal to)
#!= (not equal to)

# == is used for equals because = is used to assign a value to a variable
# print(5 +3) # 8
# print(10 /3) # 3.3333
# print(2 * 3) # 6
# print(10 % 3) #1
#
# num_to_multiply = int(input("Pls input a number to multiply by 2 > "))
# print(num_to_multiply * 2)
#
# #strings
# str1 = "Hello"
# str2 = "world"
# print(str1 + " " + str2)
#
# #Task 1
# num1 = int(input("pls enter numer 1: >> "))
# num2 = int(input("pls enter number 2: >> "))
# print(num1 + num2)
#
# # task 2
# print("Hi * 3")
#
# #task 3
#
# a = 10
# b = 5
# if a > b:
#     print( a, "is greater than,", b)
#
# print(10 > 5)

user_input = float(input("Enter a number: >>  "))
print(user_input)
cast_int = int(user_input)
print(cast_int)

name = str(input("Enter your name: >> "))
print("Hello" + " " + name)

height = int(input("Pls enter rectangle height >> "))
width = int(input("Pls enter rectangle width >> "))
print("The area is ", height * width)

























