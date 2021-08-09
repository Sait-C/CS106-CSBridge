"""
File: print_indices.py
-------------------
This program prints out the indices of a 5x5 grid, row by row.
"""


def main():
    for j in range(5):
        for i in range(5):
            print(f"({i},{j})", end=", ")
        print("")


if __name__ == '__main__':
    main()
