'''
You are given an array (which will have a length of at least 3, 
but could be very large) containing integers. 
The array is either entirely comprised of odd integers or 
entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N.
'''


MIN_LENGTH = 3


def check_outlier(evens, odds):
    return evens[0] if len(evens) == 1 else odds[0]


def assert_check(evens, odds, length, minLength):
    return length >= minLength and len(evens) != 0 and len(odds) != 0


def find_outlier(integers):
    items = {0: [], 1: [], }
    evens = items[0]
    odds = items[1]

    for index in range(0, len(integers)):
        int = integers[index]
        items[int % 2].append(int)
        if assert_check(evens, odds, length=index+1, minLength=MIN_LENGTH):
            return check_outlier(evens, odds)


