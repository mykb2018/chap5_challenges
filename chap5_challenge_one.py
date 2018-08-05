# Write a function that takes a number as an input and returns that number squared.

user_input_number = input("Pleaes input a number: ")
user_input_number = int(user_input_number)

def squaring_number(number_to_square):
    return number_to_square ** number_to_square

print(squaring_number(user_input_number))