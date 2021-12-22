# Question 1

def hello_name(user_name):
    print("hello_" + user_name)


hello_name('Yafet')

# Question 2


def first_odds(start, end):
    for num in range(start, end+1):
        if num % 2 != 0:
            print(num, end=" ")


first_odds(1, 100)

# Question 3


def max_num_in_list(a_list):
    print(max(a_list))


max_num_in_list([1, 15, 35, 2, 6, 19])

# Question 4


def is_leap_year(a_year):
    if(a_year % 4) == 0:
        if(a_year % 100) == 0:
            if(a_year % 400) == 0:
                print('true')
            else:
                print('false')
        else:
            print('true')
    else:
        print('false')


is_leap_year(1992)

# Question 5


def is_consecutive(a_list):
    maximum = max(a_list)
    if sum(a_list) == maximum * (maximum+1) / 2:
        print('true')
    else:
        print('false')


is_consecutive([1, 2, 3, 4, 5])
is_consecutive([1, 2, 4, 5])
