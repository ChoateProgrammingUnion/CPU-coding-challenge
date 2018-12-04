#!/usr/bin/env python3
"""
This file contains some python functional challenges. To use it,
follow the instruction under each class template and implement the function.
You should replace `raise ChallengeNotAttempted` with your code.

To run the tests, do

$ cd functional_challenge
$ python3 .

Don't worry there is no edge cases in this challenge and all input are guaranteed to be valid.

All challenges and unittests are written by Jerry Wang.
There is at least one valid solution to each challenge.
Tested on macOS 10.13.6 with python3.7

Date: Dec 4, 2018
"""


class ChallengeNotAttempted(Exception): pass


def add(a, b):
    """
    =============================
    Python Functional Challenge 0
    =============================

    Write a function that adds two integers.
    For example, add(2, 3) should return 5
    """
    
    raise ChallengeNotAttempted


def concat(a, b):
    """
    =============================
    Python Functional Challenge 1
    =============================

    Write a function that concatenate two strings.
    For example, concat("Hi","!") should return "Hi!"
    """
    
    raise ChallengeNotAttempted


def add_to_list(a_list, item):
    """
    =============================
    Python Functional Challenge 2
    =============================

    Write a function that adds an item to the end of a list
    For example, add_to_list([1, 2, 3], 4) should return [1, 2, 3, 4]
    """
    raise ChallengeNotAttempted


def third_element(a_list):
    """
    =============================
    Python Functional Challenge 3
    =============================

    Write a function that returns the third element of a list
    For example, third_element([0, 1, 2, 3, 4, 5]) should return 3
    Remember, index starts from 0
    """
    raise ChallengeNotAttempted


def int_to_str(n):
    """
    =============================
    Python Functional Challenge 4
    =============================

    Write a function that casts an integer to a string
    For example, int_to_str(5) should return "5"
    """
    raise ChallengeNotAttempted


def self_introduction(name, age):
    """
    =============================
    Python Functional Challenge 5
    =============================

    Write a function that returns a simple self introduction sentence:
    "Hi my name is ___ and I'm ___ years old"
    
    For example, self_introduction("Mike",18) should return  "Hi my name is Mike and I'm 18 years old"
    """
    raise ChallengeNotAttempted


def sum(*nums):
    """
    =============================
    Python Functional Challenge 6
    =============================

    Write a function that calculates the sum of some numbers
    For example, sum(1, 2, 3, 4, 5) should return 15
    """
    raise ChallengeNotAttempted


def max(*nums):
    """
    =============================
    Python Functional Challenge 7
    =============================

    Write a function that calculates the maximum number in all inputs.
    For example, max(10, 8, 2, 1, 3, 0, 22, -5) should return 22
    -10000 < n < 10000
    """
    raise ChallengeNotAttempted


def create_dict(*pairs):
    """
    =============================
    Python Functional Challenge 8
    =============================

    Write a function that creates a dictionary from input pairs.
    For example, create_dict((1, 2), (3, 4), (5, 6)) should return {1: 2, 3: 4, 5: 6}
    """
    raise ChallengeNotAttempted


def flatten(a_list):
    """
    =============================
    Python Functional Challenge 9
    =============================

    Write a function that flattens a list.
    For example, flatten([1, 2, [3, [4, 5]]) should return [1, 2, 3, 4, 5]
    """
    raise ChallengeNotAttempted
