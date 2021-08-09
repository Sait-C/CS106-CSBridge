"""
File: khansole_academy.py
-------------------
This program generates random addition problems for the user to solve, and gives
them feedback on whether their answer is right or wrong.  It keeps giving them
practice problems until they answer correctly 3 times in a row.
"""


# This is needed to generate random numbers
import random


def generateTwoRandomNumbers(min, max):
  a = random.randint(min, max)
  b = random.randint(min, max)
  return a, b

def main():
  correctCount = 0
  while True:
    a, b = generateTwoRandomNumbers(10, 99)
    correctResponse = a + b
    print("What is " + str(a) + " + " + str(b) + " ?")
    userResponse = int(input("Your answer: "))
    if userResponse == correctResponse:
      correctCount += 1
      print("Correct! You've gotten " + str(correctCount) + " correct in a row.")
      if correctCount == 3:
        print("Congratulations! You mastered addition.")
        break
    else:
       correctCount = 0
       print("Incorrect. The expected answer is " + str(correctResponse))



if __name__ == "__main__":
    main()
