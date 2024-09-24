'''
Write a Python function named print_diamond that takes an odd integer
n as an argument and prints a diamond shape with a width of n using the * character.
Note: If an even number is passed, the function should return "Please provide an odd integer."
'''

# pseudocode

# Define print_diamond function
def print_diamond(n):
    # If n is even
        if n % 2 == 0:
            # Print "Please provide an odd integer."
            print("Please provide an odd integer.")
        # If n is odd
        if n % 2 != 0:
            # Print n lines of n characters "*" on each line
            for i in range(n//2 + 1):
                print(" " * (n//2 - i) + "*" * (2 * i + 1))
            for i in range(n//2 -1, -1, -1):
                print(" " * (n//2 - i) + "*" * (2 * i + 1))
            print()


# Test print_diamond function with user input
try:
    input_integer = int(input("Enter an odd integer: "))
    print_diamond(input_integer)
except:
    print("Error: Invalid input. Please enter a valid integer.")