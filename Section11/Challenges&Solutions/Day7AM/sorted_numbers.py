"""
File: sorted_numbers.py
-------------------
This program prompts the user for 10 numbers, and then
prints out those numbers in sorted order.
"""


def main():
    inputs = get_input()
    #sort
    inputs.sort()
    show_elements(inputs)


def show_elements(list):
    for element in list:
        print(element)

def get_input():
    input_list = []
    for i in range(10):
        number = int(input("> "))
        input_list.append(number)
    return input_list
if __name__ == '__main__':
    main()
