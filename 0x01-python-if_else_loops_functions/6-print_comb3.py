#!/usr/bin/python3
# Loop from 0 to 9 for the first digit
for num1 in range(10):
    # Loop from i + 1 to 9 for the second digit
    for num2 in range(num1 + 1, 10):
        # Print the two digits with a comma and a space after each one
        if num1 == 8 and num2 == 9:
            print("{}{}".format(num1, num2, end=""))
        else:
            print("{}{}".format(num1, num2), end=", ")
# Print a new line
