"""
File: area_calculator.py
-------------------
This program can calculate the area of a circle with a radius that
is entered by the user.  It also prints out if the user has entered
an invalid (0 or negative) radius.
"""

# This line is needed to use the value of pi
import math

def checkPositive(num):
    return num >= 0

def getRadius():
    while True:
     radius = int(input("Please enter a circle radius: "))
     if checkPositive(radius):
         return radius
     else:
         print("Error! You entered an invalid radius.")

def main():
    radius = getRadius()
    area = math.pi * (radius * radius)
    print("The area of your circle is: " + str(area))

if __name__ == '__main__':
    main()
