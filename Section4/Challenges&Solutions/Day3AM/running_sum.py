"""
File: running_sum.py
-------------------
This program reads in integers from the user
and then keeps outputting the sum of the entered values.
"""


def main():
    inputCount = 0
    sumOfNums = 0
    while True:
        num = int(input("Please enter an integer:"))
        inputCount += 1
        sumOfNums += num
        print(f"The current sum is: {sumOfNums} ({inputCount} integers entered)")


if __name__ == '__main__':
    main()
