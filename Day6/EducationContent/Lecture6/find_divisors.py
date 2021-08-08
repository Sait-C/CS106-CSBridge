"""
File: find_divisors.py
--------------------
This program outputs divisors of all numbers in
range [50, 60]. The program should print "prime"
if there are no divisor found except 1 and the
number itself
"""

def main():
    min_val = 50
    max_val = 60

    for i in range(min_val, max_val + 1):
        print(str(i) + ": ", end=" ")
        # check divisibility of i by all values in range 2 to i-1
        is_prime = True  # assume the value to be prime
        for candidate in range(2, i):
            if i % candidate == 0:
                print(str(candidate) + " ", end=" ")
                is_prime = False  # a divisor is found, the number is not prime
        if is_prime:
            print("is a prime number")
        else:
            print()  # this is simply to move to the next line


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
