"""
File: divisible.py
--------------------
This program outputs all numbers divisible by 5
in a user defined range (a minimum number and a maximum number)
"""

def main():
    divisor = 5

    min_val = int(input("Specify the minimum value:"))
    max_val = int(input("Specify the maximum value:"))

    #Swap if minimum is higher than maximum
    if min_val > max_val:
        #Report to user about the swap operation
        print("Your minimum value was bigger than max value")
        print("I'll swap them for you")
        #use a temporary variable for swapping
        temp = max_val
        max_val = min_val
        min_val = temp
        print("Min-value:" + str(min_val) + ", max-value: " + str(max_val))

    for i in range(min_val, max_val + 1):
        if i % divisor == 0:#checking divisibility using the modulus operator
            print(str(i) + " is divisible by " + str(divisor))

    # # Alternative implementation using a while loop (less preferable)
    # i = min_val
    # while i <= max_val:
    #     if i % 5 == 0:
    #         print(str(i) + " is divisible by " + str(divisor))
    #     i += 1

    # # Alternative implementation, using slicing
    # # convert min and max value to closest divisible values with the range
    # min_val = (min_val // divisor + 1) * divisor
    # max_val = (max_val // divisor) * divisor
    # for i in range(min_val, max_val + 1, divisor):
    #     print(str(i) + " is divisible by " + str(divisor))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
