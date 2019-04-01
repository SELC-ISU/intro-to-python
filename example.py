# import statements in python :) 
# require importing from pip or anaconda typically 
# we can use matplotlib as a visualization software
import matplotlib.pyplot as plt

# this is a function call in Python
# also we use snake_case in python! anyone who uses camelCase in Python is probably a fool 
def this_is_a_function():
    # print statement in Python:
    print("This is a function")

# read input in python
# 100x better than a scanner
def let_me_read():
    # new with python 3! whatever is inputed is automatically stored as the type that was typed in
    # i.e no errors for not using a string or not using a number
    typed = input("enter a number: ")
    #  get the length
    print("Length:", len(typed))
    print("Word typed", typed)

this_is_a_function()
let_me_read()
print("Now we can use input with a string and get the length")
let_me_read()

# what about data structures like arrays?
# what if we used something better? Like a list
def data_types_simple():
    # A list is basically like a arrayList in Java but a bit more malleable-- Python gives the programmer the capability
    # and trust to do a lot of different things 
    my_list = ['Ann', 'Alexis', 'Angela', 'SteVen', 'Colton']
    # what will this print??
    # print(my_list[1])
    return my_list

# but ann, what if we want to make python object oriented?
# thats a thing too. We can easily make a class within a python file :)
# class declaration below:
class Student(object):
        # initializer (a .set() method if you will)
        def __init__(self, name, major, phone_number):
                super(Student,self).__init__()
                self.name = name
                self.major = major
                self.phone_number = phone_number
        # basically a toString method
        def __str__(self):
            return "Student:\n" + "Name: " + self.name +  "\nMajor: " + self.major + "\nNumber: " + self.phone_number

my_list = data_types_simple()
student_1 = Student(my_list[0], 'Software Engineering', '5158675309')
print(student_1)
# But Ann! I want more than just a list data structure! I want a hashmap!
# okayyyyy...
def data_types_not_simple(people):
    # introducing dictionaries! Super easy to use.
    # declaring
    my_dict = {"peer mentors": people}
    my_dict['advisors'] = ['Jason', 'Teela', 'Patrick']
    print(my_dict)

data_types_not_simple(my_list)

# SETS (part of our next portion so pay attention)
def sets():
    # a set removes duplicates
    print("original: abracadabra")
    a = set("abracadabra")
    print(a)

sets()