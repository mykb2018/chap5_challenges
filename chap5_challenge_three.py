# Write a function that takes three required parameters and two optional parameters.

import random

number_a = random.randint(1, 10)
number_b = random.randint(11, 20)
number_c = random.randint(21, 30)

def func_with_parms(a, b, c, d=100, e=1000):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

func_with_parms(number_a, number_b, number_c)
