"""
File: range_examples.py
--------------------
A series of range examples for you to consider
"""

def main():
    print("Output for: range(5) ", end=' ')
    for i in range(5):
        print(i, end=' ')
    print()

    print("Output for: range(5, 10) ", end=' ')
    for i in range(5, 10):
        print(i, end=' ')
    print()

    print("Output for: range(6, 15, 3) ", end=' ')
    for i in range(6, 15, 3):
        print(i, end=' ')
    print()

    print("Output for: range(15, 6, -3) ", end=' ')
    for i in range(15, 6, -3):
        print(i, end=' ')
    print()
    
    # Add your experiments here using different values in range()

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
