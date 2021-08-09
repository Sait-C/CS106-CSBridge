"""
File: moon.py
------------------
Converts weight on earth into weight on the moon.
"""


def main():
    weight = int(input("Enter a weight on Earth:"))
    weightOnTheMoon = (weight * 16.5) / 100
    print("Your weight on the moon is", weightOnTheMoon)


if __name__ == "__main__":
    main()
