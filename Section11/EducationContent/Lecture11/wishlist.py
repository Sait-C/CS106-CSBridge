"""
File: wishlist.py
---------------------
This program exemplifies the use of lists for reading a number of inputs from
the user and printing them. The program asks for new input until the user clicks
enter without typing a wish. Then program prints that some of the wishes will be fulfilled.
"""
import random


def main():
    # Creating an empty list as container of wishes
    wish_list = []
    # Read the first wish
    wish = input("Enter your wish: ")
    # As long as the input has some characters continue adding them to the list
    while len(wish) > 0:
        # add wish to the back of wish_list as a new element, wish_list grows by one element
        wish_list.append(wish)
        # ask for another wish
        wish = input("Enter your wish: ")

    print("Thanks for entering all your wishes, let's see what we can do about those")
    # do something with the wishes
    for i in range(len(wish_list)): # the length of the wish_list is accessible
        wish_remembered = wish_list[i]
        if random.choice([True, False]):
            print("I'll get you " + wish_remembered +  ", no worries")
        else:
            print("Sorry, I cannot get you " + wish_remembered)


if __name__ == '__main__':
    main()
