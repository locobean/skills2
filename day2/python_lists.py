'''# Lists
#lists are ordered, mutable, and allow duplicates

coaches_lists = [ "Callum", "Aiden", "Sandra", "Remi"]
print(len(coaches_lists)) #check length of str, list etc

# List indexing
print(coaches_lists [0])
print(coaches_lists [1])
print(coaches_lists [2])
print(coaches_lists [3])

#up to 3rd element
print(coaches_lists [:3])

# Elements after 2: index 2 after
print(coaches_lists[2:])

# Elements from 1 and 3 index
print(coaches_lists[1:3])

# returns a bool
print("Callum" in coaches_lists)

# change item in list
coaches_lists[1] = "Bob"
print(coaches_lists)

# Change list with multiple items
coaches_lists[1:2] = ["George","Jill"] # 1 start up to 2 in index
print(coaches_lists)

# Negative indexing
print(" The last coach is ", coaches_lists[-1])

x = "cool"
print(x[-1])

# List Methods
num_list = [1,5, 6, 3, 75, 2]

# Insert value
num_list.insert(2, 450)
print(num_list)



# Remove the last item in the list
num_list.pop()
print(num_list)

# Remove a specific index value
num_list.pop(1)
print(num_list)

# Sort the list
num_list.sort(reverse=True) # prints in largest to smallest
print(num_list)

# Add a value to the end of the list
num_list.append(45)
print(num_list)

# Slicing
my_list = [10, 20, 30, 40, 50, 60, 70]

# Negative slicing
print(my_list[-7::1])

# Arrays
# Arrays are similar to lists but only store numbers

import array as arr
# The i declares the data type of the array
my_arr = arr.array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(type(my_arr))

# Access parts of an array
print(my_arr[0])
print(my_arr[1])
print(my_arr[-1])

# Casting a list to an array
num_list2 = [2,5,10,43,27,19]
num_arr = arr.array("i", num_list2)
print(num_arr)

#slicing an array
print(num_arr[2:5])
print(num_arr[:5])
print(num_arr[:-4])

# Changing elements in an array
num_arr[0] = 1
print(num_arr)
num_arr[2:5] = arr.array("i", [5,6,7])
print(num_arr)

# concatination
to_five = arr.array("i", [1,2,3,4,5])
to_ten = arr.array("i", [6,7,8,9,10])

number = arr.array("i") #empty array
numbers =  to_five + to_ten
print(numbers)

# del an element
del numbers[2]
print(numbers)

# Array Methods
nums = arr.array("i", [1,2,3])
# APPEND
nums.append(4)
print(nums)

# Extend
nums.extend([5,6])
print(nums)

#pop()
nums.pop()
print(nums)

nums.pop(2)
print(nums)

#count th enumber of times a number occurs in an array
new_nums = arr.array("i", [1,2,3,4,4,5,5])
print(new_nums.count(5)) '''

# Creation of a five times table list called five_x_table.

five_x_table = [] # declare list

five_x_table.append(5 * 1) # start 5 * table append result to index
five_x_table.append(5 * 2)
five_x_table.append(5 * 3)
five_x_table.append(5 * 4)
five_x_table.append(5 * 5)
five_x_table.append(5 * 6)
five_x_table.append(5 * 7)
five_x_table.append(5 * 8)
five_x_table.append(5 * 9)
five_x_table.append(5 * 10) # end 5 * table append result to index
print(five_x_table) # print list


remove = five_x_table.pop(2) # removes value at index position 2
print(five_x_table) # Prints list
print("The value", remove, "was removed.") # removed value

five_x_table.insert(2, remove) # Inserts remove value back into index.
print(five_x_table)
print("The value", remove, "was inserted back into the index 2.")

del five_x_table[-1] # uses del module to remove last element
print(five_x_table)
print("The last element was removed from the list using del method.")

print("The filth element is",(five_x_table[4])) # Prints 5th element in the index list.

pos = five_x_table.index(40) #find number 40 position in index.
print(pos)

count = five_x_table.count(30) # Count how many times 30 appears in the list.
print(count)

















