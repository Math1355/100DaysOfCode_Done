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
