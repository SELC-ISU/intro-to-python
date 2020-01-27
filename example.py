'''
Import statements in python (a unique aspect of Python)
Typically utilizes pip or anaconda (conda)
'''
# import matplotlib.pyplot as plt #matplotlib is used a lot for data science visualizationn


'''
This is a function call in python.
Python uses "snake_case" **google if confused... tldr; notation is different from CamelCase
'''
def this_is_a_function():
    # print statement in Python:
    print("This is a function")

'''
Reading input in Python (another unique aspect: Python is super easy to pick up)
'''
def let_me_read():
    typed = input("enter a number: ")
    #  get the length
    print("Length:", len(typed))
    print("Word typed:", typed)
    print("Type:", type(typed))

# CHECKPOINT 1 : THE BASICS 
def checkpoint1():
    this_is_a_function()
    print("Now we can use input with a string and get the length")
    let_me_read()

'''
What about data structures like arrays?
Python utilizes lists! which are dynamic arrays basically
(another unique Python thing: being a bit "dynamic" in this sense)
'''
def data_types_simple():

    my_list = ['Ann', 'Alexis', 'Angela', 'SteVen']
    my_list.append('Andrew')
    # what will this print??
    return my_list


'''
MAKING PYTHON OOP (easy peasy)
Another unique aspect of Python: everything technically is typed but you don't have to declare variables w a type
Here's an example of a class in python:
'''
class Student(object):
        # initializer (a .set() method if you will)
        def __init__(self, name, major, phone_number):
                super(Student,self).__init__()
                self.name = name
                self.major = major
                self.phone_number = phone_number

        def __str__(self):
            return "Student:\n" + "Name: " + self.name +  "\nMajor: " + self.major + "\nNumber: " + self.phone_number

# CHECKPOINT 2 : SIMPLE TYPES / OOP
def checkpoint2():
    my_mentors = data_types_simple()
    print(my_mentors)
    student_1 = Student(my_mentors[1], 'Software Engineering', '5158675309')
    print(student_1)

'''
"HASHMAPS" IN PYTHON:

What if I want to associate specific data in a KEY/VALUE manner?
Python has a data type call a dictionary. 
'''
def data_types_not_simple(people) -> dict:
    my_dict = {"peer mentors": people}
    my_dict['advisors'] = ['Jason', 'Teela', 'Patrick']
    return my_dict

'''
SETS: Remove duplicate instances from a list in this unique data type
Very similar to list though.
'''
def sets():
    # a set removes duplicates
    print("original: abracadabra")
    a = set("abracadabra")
    print(a)


# CHECKPOINT 3 : Different Data Types
def checkpoint3():
    print(data_types_not_simple)
    sets()


def main():
    checkpoint1()
    # checkpoint2()
    # checkpoint3()

if __name__== "__main__":
    main()
