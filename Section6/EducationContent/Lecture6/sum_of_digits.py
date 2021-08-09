"""
File: sum_of_digits.py
--------------------
This program computes the sum of all digits of an integer read from the user.
It continues asking user input as long as the integer specified is positive.
"""


def main():
    while True:
        #Read user input
        num = int(input("Enter a positive integer: "))
        if num < 0:
            break
        # Computing sum of digits
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        print("Sum of all digits: " + str(digit_sum))
    print("BYE")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
