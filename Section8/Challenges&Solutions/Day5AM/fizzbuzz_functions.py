"""
File: fizzbuzz_functions.py
--------------------
This program plays the game fizzbuzz up to a given number entered by the user.
"""


def main():
    # TODO: your code here (remove the 'pass' when you start)
    count = int(input("Number to count to: "))
    numberOfFizzOrBuzz = fizzbuzz(count)
    print(f"{numberOfFizzOrBuzz} numbers were fizzed or buzzed")


def fizzbuzz(n):
    """
    Plays the fizzbuzz game up to and including n.  It prints out numbers from 1 to n,
    except if the number is divisible by 3, it instead prints "Fizz", if the number
    is divisible by 5, it instead prints "Buzz", and if it is both, instead it prints "FizzBuzz".
    This function returns the count of numbers that were replaced.
    """
    numberOfFizzOrBuzz = 0
    for i in range(1, n + 1):
        is_Fizzbuzz, out = check_fizz_buzz(i)
        if is_Fizzbuzz:
            numberOfFizzOrBuzz += 1
        print(out)
    return numberOfFizzOrBuzz

def check_fizz_buzz(num):
    if (num%3 == 0) and (num % 5 == 0):
        return True, "Fizzbuzz"
    elif (num%3 == 0):
        return True, "Fizz"
    elif (num%5 == 0):
        return True, "Buzz"
    else:
        return False, str(num)
if __name__ == "__main__":
    main()
