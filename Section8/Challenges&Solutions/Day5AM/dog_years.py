"""
File: dog_years.py
--------------------
This program prints out the number of dog years for a given number
of human years.
"""


DOG_YEARS_PER_HUMAN_YEAR = 7

def main():
    user_input = int(input("Enter an age in human years: "))
    while user_input != 0:
        if user_input < 0:
            print("Sorry, please enter a positive number or 0 to exit")
        else:
            # TODO: your code here (remove the 'pass' when you start)
            dogYears = compute_dog_years(user_input)
            print("The age in dog years is " + str(dogYears))
        user_input = int(input("Enter an age in human years: "))


def compute_dog_years(human_years):
    """
    Takes in a number of human years and returns its conversion to dog years.
    """
    return human_years * DOG_YEARS_PER_HUMAN_YEAR


if __name__ == "__main__":
    main()
