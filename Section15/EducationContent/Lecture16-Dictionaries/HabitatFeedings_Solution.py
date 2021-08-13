"""
CS Bridge 2020
The program captures data about animals, their diet and feeding times using dictionaries
Author: Ayca Tuzmen
"""

def create_animal_diet():
    """
    Create a dictioary which contains information about an animal
    and its diet
    """
    d = {}
    d['elephant'] = 'grass'
    d['bear'] = 'bearies'
    d['otter'] = 'clams'
    d['playthus'] = 'shrimp'
    print(d)
    return d
def create_animal_feeding_times():
    """
        Create a dictioary which contains information about an animal
        and its feeding times per day
        """
    d = {'elephant':2, 'bear':1, 'otter': 3, 'playthus': 4}
    d['bear'] += 1
    print(d)
    return d
def print_all(names_diet, names_feeding_times):
    """
        Prints the data stored in two dictionaries and shows the animal, its diet and it
        feeding times per day
    """
    for name in names_diet.keys():
        print(name, 'eats', names_diet[name], names_feeding_times[name], 'times a day.')

def main():
    names_diet = create_animal_diet()
    names_feeding_times = create_animal_feeding_times()
    print_all (names_diet, names_feeding_times)


if __name__ == '__main__':
    main()