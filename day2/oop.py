# oop - allows us to model real-world entities in code
# Key differences
    # encapsulation
    # objects
    #methods - functions 'belong' to specific objects

# main terms for us to understand effectively begin modelling objects and data
    # The class -  this is the entity we are modelling (eg car, animal, person) - blueprint

    # The Object - this is the house - the instance of the class/instance, which has data and behaviours attached to it (eg bmw, dog, sam)

    # Attributes - this is the info or data that relates to the object, on the class we donate what data is related to the entity we are modelling

    # Methods - this is the behaviour / the  things it can do, on the class we define the details of this behaviour (functionality)

    # the constructor - this is a special method which sets the data to the objects when instantiated


class GradeBook:
    def __init__(self, grades):
     self.grades = grades # data belongs to the object

    def calculate_average(self):
        total = sum(self.grades)
        return total / len(self.grades)

    def display_average(self):
        average = self.calculate_average()
        print('Average Grade:', average)

def main():
    gradebook = GradeBook([85, 90, 78, 92, 88])
    gradebook.display_average()

main()

# OOP pillars
    # abstraction - hide implementation details and show only essential features - works internally just how to use it
    # achieved in python via abstract base classes

    # encapsulation - control over data /attributes of a class. We can ensure attributes con only be updated from within a class
    # achieved in python using public (everywhere), protected (child classes) (_)
    # private (this class only) (__)

    # polymorphism - same method name can behave differently depending on the object
    # achieved in python using
        # method overriding (same method, different number of arguments)

    # inheritance - allows a  child class to reuse and extend functionality from another class (parent)
    # in python
        # a child class inherits using parenthesis: class child(parent)
        # support single and multiple inheritance
        # super() function calls methods from parent class



# main terms for us to understand to effectively begin modelling objects and data...

# the class - this is the entity we are modelling (e.g. the Car, the Animal, the Person, the House)


# the object - this is the instance of the class/instance, which has data and behaviours attached to it (e.g. the BMW, the Dog, the Sam)


# the attribute - this is the info, or the data, that relates to the object... on the class we denote what data is related to the entity we are modelling... on the object we assign actual value to these data points


# the methods - this is the behaviour / the things it can do, on the class we define the details of this behaviour (the functionality)


# the constructor - this is a special method which sets our data to the objects when instantiated






