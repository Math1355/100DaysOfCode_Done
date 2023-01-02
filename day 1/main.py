'''
Create a function that takes the age and return the age in days.

Notes
Use 365 days as the length of a year for this challenge.
Ignore leap years and days between last birthday and now.
Expect only positive integer inputs.
'''

import age_calculator


def menu_calculator():
    print("=-" * 18)
    print("=-" * 5 + " AGE CALCULATOR " + "=-" * 5)
    print("=-" * 18)

    age = int(input("Enter your age: "))
    while age < 0:
        age = int(
            input("Your age cannot be less than zero, Please enter a valid age: "))

    age_calculator.calculator(age)


if(__name__ == "__main__"):
    menu_calculator()
