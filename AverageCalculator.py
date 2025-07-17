"""
Filename: AverageCalculator
File-type: .py
Author: Andrei Alexandru
Date: 10.06.2022
About: A program that uses the user input, that should be a numeric value(integer - positive, negative and float),
       and creates a median value and average.
"""

# Creating a list for the numbers, the list can be displayed with the command 'numbers'.
numbers = []


# Beginning instructions.
def instruction():
    print("Welcome to the average calculator!")
    print("You can start typing your numbers right away or type 'rules' to see the instructions of the program.")


instruction()


# Function that stores all the rules of the program.
def rules():
    # Creating a command to display the numbers inserted in the list in ascending order.
    if i == "numbers":
        if len(numbers) == 0:
            print("You haven't introduced any numbers yet.")
        else:
            print(sorted(numbers))
            print("If you want to add more numbers to the list type them below. ↓")
            print("If you want to quit the program type 'quit', to calculate the average type 'average'.")
    # Creating a command to quit the program.
    elif i == "quit":
        print("Thank you for using Average Calculator!")
        quit()
    # Creating a command to display the rules.
    elif i == "rules":
        print("To see the list with the numbers inserted type 'numbers'.")
        print("To calculate the average type 'average'.")
        print("To quit the program type 'quit'")
    # From the function rules if the rules do not apply to the input the function 'invalid_values()' will be called.
    else:
        invalid_values()


# Function for invalid values.
def invalid_values():
    if not i.isdigit():
        print("Invalid Value!")
    elif i == "0":
        print("Please insert a number greater, smaller or equal to 1!")
    # If the input is a character besides a message is going to be displayed.
    else:
        if i.isalpha() and i not in ("average", "rules", "numbers", "quit"):
            print("Invalid value!")


# Function that checks if a number is a float
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


while True:
    # Assigning input/Making it case-insensitive.
    i = input("Enter your numbers here: ").lower()
    # Checking if the string is a number and if is true adding it to a list as an integer.
    if i.isdigit() and i != "0":
        numbers.append(int(i))
    # If the number is a float is going to be added in the list
    elif isfloat(i):
        try:
            if i != "0":
                numbers.append(float(i))
        finally:
            if i == "0":
                rules()
    # If the string is not a number and the string is 'average' the program will calculate the average
    # and median number
    else:
        # Rules and formula for average calculation.
        if i == "average" and len(numbers) == 0:
            print("Please insert at least 1 number!")
        elif i == "average" and len(numbers) >= 1:
            avr = sum(numbers) / len(numbers)
            n = len(numbers)
            numbers.sort()
            # Finding the middle 2 numbers if the number of elements in the list is even.
            if n % 2 == 0:
                # Finding median number 1
                mn_1 = numbers[n // 2]
                # Finding median number 2
                mn_2 = numbers[n // 2 - 1]
                m = (mn_1 + mn_2) / 2
                # Printing the average and median number.
                print("Your average is: {} and your median number is: {}.".format(avr, m))
                # Adding retry command.
                answer = str(input("Try again? (y/n): ")).lower()
                # If the answer is 'y' the elements from the list will be cleared.
                if answer == "y":
                    numbers.clear()
                    instruction()
                    continue
                # If the answer is no the program is going to close and a farewell message is going to be printed.
                elif answer == "n":
                    print("Thank you for using Average Calculator!")
                    break
                # If the answer in not 'y' or 'n' a message is going to appear.
                else:
                    if answer not in ("y", "n"):
                        print("Invalid Value")
                        break
            # Finding the middle number if the number of elements in the list is odd.
            else:
                m = numbers[n // 2]
                print("Your average is: {} and your median number is: {}.".format(avr, m))
                answer = str(input("Try again? (y/n): ")).lower()
                if answer == "y":
                    numbers.clear()
                    continue
                elif answer == "n":
                    print("Thank you for using Average Calculator!")
                    break
                else:
                    if answer not in ("y", "n"):
                        print("Invalid Value")
                        break
        # If the input doesn't match any of the code above the function 'rules()' will be called.
        else:
            rules()
