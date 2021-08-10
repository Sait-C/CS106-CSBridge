"""
File: is_ascending.py
-------------------
This program prompts the user for numbers until they enter -1, and then
prints out the numbers and whether or not those numbers are in ascending order.
"""

def main():
    inputs = get_input()
    show_elements(inputs)
    print(check_is_ascending(inputs))

def check_is_ascending(list):
    previous_element = float("-inf")
    for element in list:
        if element < previous_element:
            return "Not ascending"
        previous_element = element
    return "Ascending!"

def show_elements(list):
    for element in list:
        print(element)

def get_input():
    inputs = []
    num = int(input("> "))
    while num != -1:
        inputs.append(num)
        num = int(input("> "))
    return inputs

if __name__ == '__main__':
    main()
