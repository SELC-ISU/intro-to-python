'''
SOME LITTLE THINGS THAT MAKE PYTHON ~UNIQUE~ FROM OTHER LANGUAGES:
'''

# LIST COMPREHENSION
'''
Typically a concise way to make/modify lists (arrays) in Python
Cool way to impress people in interviews :')
'''
# GROSS! So many lines.
def is_even_og(pass_in: list):
    is_even = []
    for i in pass_in:
        if i % 2 == 0:
            is_even.append("YES")
        else:
            is_even.append("NO!")
    print(is_even)

# not as many lines now... try to draw connections between the two
def is_even_lc(pass_in: list):
    is_even = ["YES" if i % 2 == 0 else "NO!" for i in pass_in]
    print(is_even)

# DECORATORS *PROBABLY THE TRICKIEST THING*
'''
Decorators add functionalities to methods in Python... Imagine if you wanted to "preprocess something" before another method executes.
Remember technically everything in python has a type! Even function instances.
Typically I see decorators being used with things like API calls + validation (user needs to be authorized BEFORE making API call)
This is a really REALLY basic example. you can do cool things with decorators
We can call functions within other functions

psuedo api call: 
'''

def my_api_call(func):

    def is_user_authed(*args):
        print(func(*args))

    return is_user_authed

def user_authed(name: str):
    if name == "Ann":
        return "STATUS CODE: 200"
    return "STATUS CODE: 403"

# DUNDER/MAGIC METHODS 
'''
Dunder (double underscore) methods are used to overwrite operator overloading when utilizing OOP in Python... We're going to reuse our
example from 186's Pokemon code!

EXAMPLE:
'''
class Pokemon:

    def __init__(self, name: str, personal_name: str, elemental_type: str):
        self.name = name
        self.personal_name = personal_name
        self.elemental_type = elemental_type


    # def __str__(self):
    #     return " POKEMON NAME: %s\n PERSONAL NAME: %s\n ELEMENTAL TYPE: %s\n" % (self.name, self.personal_name, self.elemental_type)


def main():
    # LC
    my_list = [1,2,3,4,5,6,7,8]
    # is_even_lc(my_list)
    # is_even_og(my_list)

    # Decorators
    call = my_api_call(user_authed)
    call("Ann")
    # DUNDER
    pika = Pokemon(name="pikachu", personal_name="pwn man", elemental_type="electric")
    #  what happens when we comment out the __str__ method above in the Pokemon class?
    #  print(pika)

if __name__ == '__main__':
    main()

