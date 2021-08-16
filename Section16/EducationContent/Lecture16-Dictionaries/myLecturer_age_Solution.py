"""
CS Bridge 2020
The program captures data about people and their age using dictionaries
Author: Ayca Tuzmen
"""
def create_dic():
    d = {'ayca': 34, 'nick': 28, 'ondrej': 30, 'chris':29}
    return d

def print_dic(d):
    print(d)
    for name, age in d.items():
        print(name, 'is', age, 'years old')

def print_sorted_names(d):
    sorted_names = list(sorted(d))
    for name in sorted_names:
        print (name)

def print_sorted_ages(d):
    sorted_ages = list(sorted(d.values()))
    for age in sorted_ages:
        print (age)
def main():
    d = create_dic()
    print_dic(d)
    print_sorted_names(d)
    print_sorted_ages(d)


if __name__ == '__main__':
    main()