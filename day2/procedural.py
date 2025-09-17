# line by line

# example of procedural python programming

#step 1 - collect grades
def get_grades():
    grades = [85, 90, 78, 92, 88] # hard coded
    return grades

# step 2 - process grades (calc total and avg)
def calculate_average(grades):
    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)
    return average

def display_average(average):
    print("The class average is", average)

def main():
    grades = get_grades()
    average= calculate_average(grades) # process data
    display_average(average)

main() # call main function




