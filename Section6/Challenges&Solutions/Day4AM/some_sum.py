"""
File: some_sum.py
-------------------
This program reads in 10 numbers from the user and prints
out the sum of those 10 numbers.
"""


def main():
    sumOfNumbers = 0
    for i in range(10):
      value = int(input("Please enter the number " + str(i + 1) + ": "))
      sumOfNumbers += value
    print("The sum is: " + str(sumOfNumbers))


if __name__ == '__main__':
    main()
