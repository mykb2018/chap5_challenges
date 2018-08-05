# Write a function that converts a string to a float and returns the result.
# Use execption handling to catch the exception that could occur.

def exception_handling():
    try:
        user_input = input("Please input float number: ")
        print(float(user_input))
    except ValueError:
        print("Invalid Value.")


exception_handling()