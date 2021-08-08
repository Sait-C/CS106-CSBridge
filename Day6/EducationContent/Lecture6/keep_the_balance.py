"""
File: keep_the_balance.py
--------------------
Program to solve the riddle:
"I have a factory that runs with 100 people.
Some people get paid 500 units/month, some
100 units/month, and some 5 units/month.
I pay 10000 units/month to my workers.
How many of the 100 receive 5 units/month?"
"""


def main():
    total_paid = 10000
    salary_cat_1 = 500
    salary_cat_2 = 100
    salary_cat_3 = 5
    total_num_workers = 100

    for num_worker_cat_1 in range(total_paid // salary_cat_1):
        for num_worker_cat_2 in range(total_paid // salary_cat_2 - num_worker_cat_1):
            num_worker_cat_3 = total_num_workers - (num_worker_cat_1 + num_worker_cat_2)
            paid = num_worker_cat_1 * salary_cat_1 + num_worker_cat_2 * salary_cat_2 + num_worker_cat_3 * salary_cat_3
            if paid == total_paid:
                print('Number of workers in category 1 = ' + str(num_worker_cat_1))
                print('Number of workers in category 2 = ' + str(num_worker_cat_2))
                print('Number of workers in category 3 = ' + str(num_worker_cat_3))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()



