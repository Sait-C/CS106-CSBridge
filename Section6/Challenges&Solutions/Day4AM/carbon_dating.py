"""
File: carbon_dating.py
------------------
This program runs carbon dating (how cool!)
First, it prints out a lookup table that maps the percent
of c14 remaining to the number of years the sample has been
dead for, for the first 20 half lives.

Then, it prompts the user to enter a percent of c14, and it
will output the age of that sample.  It will re-prompt the user
until they enter -1, at which point the program will terminate.
"""


# This is needed to use the log function
import math


# The number of years it takes for the amount of c14 to be cut in half
C14_HALF_LIFE = 5700


def printInfo():
  years = 0
  value = 100
  print("Carbon Dating Lookup Table")
  print("Percent C-14 Remaining: years passed")
  print("--------------------------")
  for i in range(20):
    print(str(value) + "% : " + str(years) + " years")
    value = value / 2
    years += C14_HALF_LIFE

def calculateAge(percent):
  return (math.log(percent/100) / math.log(1/2)) * C14_HALF_LIFE

def main():
  printInfo()
  percent = float(input("What percent of natural carbon-14 does your sample have? "))
  print(str(percent) +" carbon-14...")
  sample = calculateAge(percent)
  print("Your sample is " + str(sample) + " years old.")


if __name__ == '__main__':
    main()
