
def is_prime(number):
    if (number == 2):
        return True
    elif (number < 2):
        return False

    for x in range(2, number):
        if (number % x) == 0:
            return False
    return True

def next_prime(number):
    return number if is_prime(number) else next_prime(number + 1)


if(__name__ == "__main__"):
    next_prime()