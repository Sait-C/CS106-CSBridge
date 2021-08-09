"""
File: 8ball.py
-------------------
Simulates an eight ball and gives sage answers to
yes or no questions.
"""

# This is needed to generate random numbers
import random

#this solution is not receommended(it made with section leader)
#you can solve this solution with lists ;)
def main():
    while True:
        question = input("Ask a yes or no question: ")
        print("Your question: " + question)
        num = random.randint(1, 5)
        if num == 1:
            print("Without a doubt.")
        if num == 2:
            print("Yes.")
        if num == 3:
            print("Ask again later.")
        if num == 4:
            print("No.")
        if num == 5:
            print("Karel thinks so.")


if __name__ == '__main__':
    main()
