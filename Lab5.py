# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    message = "*" * n + ("\n*" + " " * (n-2) + "*") * (n-2)
    if n > 1:
        message += "\n" + "*" * n

    return message

# 1
# 12
# 123
# 1234
def number_pattern(n):
    message = ''    

    for x in range(1, n + 1):
        number = 0

        for y in range(x):
            number += 1
            message += str(number)

        if x != n:
            message += "\n"

    return message

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    sum = 0
    for x in range(n):
        sum += x + 1
    return sum

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    pyramid = " " * (n-1)
    return ""

# print(number_pattern(5))

