"""
File: number_combinations.py
--------------------
This program exemplifies use of nested for loops
for creation of number combinations
"""


def main():
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for m in range(2):
                    print(str(i) + str(j) + str(k) + str(m))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
