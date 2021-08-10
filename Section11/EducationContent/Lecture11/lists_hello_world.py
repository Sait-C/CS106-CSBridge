"""
File: lists_intro.py
------------------------
Introduction to lists
"""
import random

def main():
    # A list of strings
    some_str_list = ["Elma", "Armut"] # initialising the list with two elements
    some_str_list.append("Kel Mahmut") # adding new element to the list
    print(some_str_list)

    # A list containing different types of data
    mixed_list = [2, True, "Hi", 6.8]
    print(mixed_list)

    # A list of integers
    int_list = [10, 20, 30, 40, 50, 60]

    # Print elements via accessing them in a for loop
    for i in range(len(int_list)):
        print(int_list[i])

    # Creating an empty list and appending random integer values
    random_ints_list = []
    for i in range(10):
        random_ints_list.append(random.randint(0, 9))
    print(random_ints_list)

    # Accessing values of a list and modifying them
    for i in range(len(random_ints_list)):
        random_ints_list[i] *= 10
    print(random_ints_list)



if __name__ == '__main__':
    main()
