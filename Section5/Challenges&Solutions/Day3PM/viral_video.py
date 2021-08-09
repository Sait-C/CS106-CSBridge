"""
File: viral_video.py
-------------------
This program asks the user for a target number of video views
and a growth rate, and calculates how many view the video creator
will get over time and how many days it will take to get to the target
number of views.
"""


def main():
    target = int(input("Please enter the target number: "))
    rate = int(input("Please enter the growth rate: "))
    views = 1
    day = 1
    print("Day " + str(day) + ": " + str(views) + " view")
    while (views < target):
        day += 1  # day = day + 1
        views *= rate  # views = views * 3
        print("Day " + str(day) + ": " + str(views) + " views")
    print("It took you " + str(day) + " days to reach or exceed your goal of " + str(target) + " views!")


if __name__ == "__main__":
    main()
