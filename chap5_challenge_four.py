# Write a program with two functions.
# The first function should take an integer as a parameter and return the result of the integer divided by 2.
# The second function should take an integer as a parameter and return the result of the integer multiplied by 4.
# Call the first function, save the result as a variable, and pass it as a parameter to the second function.

import random

def first_function(first_parm):
    return int(first_parm / 2)


def second_function(second_parm):
    print(second_parm * 4)


number_for_parm = random.randint(1, 100)

first = first_function(number_for_parm)
second_function(first)