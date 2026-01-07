# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    square = "*" * n + ("\n*" + " " * (n-2) + "*") * (n-2)
    if n > 1:
        square += "\n" + "*" * n

    return square

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
    pyramid = ''

    for x in range(1, n + 1):
        pyramid += " " * (n - x) + "*" * (2 * x - 1)
        if x != n:
            pyramid += "\n"

    return pyramid
