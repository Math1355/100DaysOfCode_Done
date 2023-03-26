
def combination(numbers):
    options = {0:'[]', 1:'[]', 2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'], 
    7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}

    result = []

    if len(numbers) > 1 and len(numbers) <= 4:
        list_nums = []
        for number in numbers:
            list_nums.append(int(number))

        for first_letter in options[list_nums[0]]:
            for second_letter in options[list_nums[1]]:
                result.append("{}{}".format(first_letter, second_letter))

        return result
    elif len(numbers) == 1:
        list_nums = int(numbers)
        return options[list_nums]
    else:
        return "Invalid option!"

if(__name__ == "__main__"):
    combination() 