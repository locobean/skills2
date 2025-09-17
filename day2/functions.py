# functions
# block of reusable code
# call when needed
# name() define by def
# DRY - DON'T REPEAT YOURSELF!!

def hello(name): #define th efunction with name parameter
    return "Hello World! " + name # return name

name1 = hello("Sam")
name2 = hello("Morgan")
name3 = hello("Liam")

print(name1)

# function to add two numbers
def addition(num1, num2):
    return num1 + num2

print(addition(1, 2)) # print the addition result

# Function to multiply two numbers
def multiply(num3, num4):
    return num3 * num4

print(multiply(3,3)) # print the multiplied numbers

# Scope in functions
# Variables defined within a function are local to that function

def set_name():
    name = "sam"
    return name

name_result = set_name()
print(name_result)

''' def change_name():
    global global_name
    global_name = "Ollie"


global_name = "Luke"
change_name()
print(global_name) '''


# Task1 -  pass argument into function and print message result
def my_first_function(message):
    print("I love " + message + "!")

your_message = my_first_function("cheese")

#Task2 - Tripler() - multiply argument by 3 add print on separate lines

def tripler(x, y, z): # pass values
    print(x * 3)
    print(y * 3)
    print(z * 3)

trip_num = tripler(2,3, 4)

#Task 3 - greet()
def greet(name):
    print("Hello, " + name)

your_name = greet("Liam")

#Task 4 - even() - return if number is even or odd

def even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

# add number to be checked
even(11)


# Task 4 - repeat_word() number of times
def repeat_word(word, times): # word and times arguments
 for i in range(times): #for loop to loop times amount
     print(word)

repeat_word("hello", 3) # enter word and times values

# regular function

def sum(a,b):
    return a+b

# lambda equivlient
sum_lambda = lambda a,b: a + b
print(sum_lambda(3,4))
print (sum(1,2))

# challenge
import math


def circle_perimeter(radius):
    return 2 * math.pi * radius


def circle_area(radius):
    return math.pi * radius ** 2

circle_perimeter_lambda = lambda radius: 2 * math.pi * radius
print(circle_perimeter_lambda(4))


circle_area_lambda = lambda radius: math.pi * radius ** 2
print(circle_area_lambda(4))

# lambda functions in practice
# map & filter
add =lambda a, b: a+b
print(add(1,2))

# 1: lambda inside a function
def multiplier(n):
    return lambda x: x * n

print(multiplier(3))

subtract = lambda a, b, c: a + b - c
print(subtract(1,2, 3))

cube = lambda x: x**3
print(cube(3))

doubler = multiplier(2)
tripler = multiplier(3)

print(doubler(10))
print(tripler(10))

# 2: lambda functions in map and filter
# map - apply a function to each element
numbers = [2,3,4]
doubled = list(map(lambda x: x * 2, numbers)) #convert to list first first before filter & lambda
print(numbers)
print(doubled)

# filter - apply a condition to each element to filter them
numbers = [1, 10,]
evens = list(filter(lambda x: x % 2 == 0, numbers)) #convert to list first before filter & lambda
odds= list(filter(lambda x: x % 2 != 0, numbers))
print(evens)
print(odds)

# sort -arranges the numbers in ascending order and alters the existing list
numbers = [10, 3, 5, 1, 7] # list numbers
numbers.sort()        # ascending numbers
print(numbers)        # [1, 3, 5, 7, 10]

sort_numbers = sorted(numbers, key=lambda x: x % 3) #
print(sort_numbers) # sorted creates a new sorted list of the elements

sorted_numbers = sorted(numbers, key=lambda x: x % 3)
print(sorted_numbers)

# reduce - combines all element of a list into one value
from functools import reduce

numbers = [1, 2, 3, 4, 5] # adds first two elements, then next, repeating until end;
total = reduce(lambda x, y: x + y, numbers)
print(total)



# working with csv
# reading

import csv

rows = []

with open('employees.csv', 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

print(header)
print(rows)

# writing

header = ['Name', 'Age']
data = [['Alex', 25], ['Brad', 45], ['Joey', 18]]

with open('student_info.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(data)

# csv.DictReader()

with open('employees.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'], row['email'])
        print(row)

# csv.DictWriter

headers = ['Name', 'Age']
data = [['Alex', 25], ['Brad', 45], ['Joey', 18]]

with open('student_info.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)

    writer.writeheader()
    for student in data:
        writer.writerow({'Name': student[0], 'Age': student[1]})


























