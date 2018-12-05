#!/usr/bin/env python3
"""
This file contains some python OOP challenges. To use it,
follow the instruction under each class template and implement the function.
You should remove the `raise ChallengeNotAttempted` line after you start to work on the challenge.
You can also remove the `def __init__(self)` part if you believe it is unnecessary.

To run the tests, do

$ cd oop_challenge
$ python3 .

All challenges and unittests are written by Jerry Wang.
There is at least one valid solution to each challenge.
Tested on macOS 10.13.6 with python3.7

Date: Dec 4, 2018
"""


class ChallengeNotAttempted(Exception): pass


class Basic:
    """
    ================================
    Python OOP challenge level 0b000
    ================================
    
    Warming up. Write a class such that
    
    b = Basic()
    b.is_basic == True
    b.say_hi() == "Hi"
    
    """
    
    def __init__(self):
        raise ChallengeNotAttempted


class Person:
    """
    ================================
    Python OOP challenge level 0b001
    ================================
    
    There are many people around us and it's hard to remember everyone's name.
    So it's better to have something to store people's name.
    
    p = Person("Mike", 18)
    p.name == "Mike"
    p.age == 18
    p.introduction == "Hi my name is Mike and I'm 18 years old"
    str(p) == "Mike, age 18"
    
    Reassignment should change the introduction
    
    p.name = "Jerry"
    p.introduction == "Hi my name is Jerry and I'm 18 years old"
    
    Age will always be an integer greater than or equals to 2 (meaning it's always plural).
    
    Hint: @property
    """
    def __init__(self,name, age):
        raise ChallengeNotAttempted
    

class WeirdNumber:
    """
    ================================
    Python OOP challenge level 0b010
    ================================
    
    Once upon the time, there was a weird number. Nobody knew what it was, but it existed.
    Some weird people called it infinity, although nobody knew what that word meant either.
    It seemed to be able to defy the rules of all basic mathematical operations, that is
    
    Let n be some random integer or float point number.
    Let w be the weird number
    
    w + n == w
    w + w == w
    
    w - n == w
    w - w == 0
    
    w * n == w
    w * w == Nan
    W * 0 == 0
    
    w / n == w (n!=0)
    w / w == 1
    w / 0 == NaN
    
    w > n
 
    There is, of course, only one such weird number. So it always equals to itself.
    But it never equals to anything else.
    WeirdNumber() == WeirdNumber()
    w != n
    
    Hint: to construct an instance of NaN (not a number), use float("NaN")
    """
    
    def __init__(self):
        raise ChallengeNotAttempted


class Dictionary:
    """
    ================================
    Python OOP challenge level 0b011
    ================================
    
    Write a class that acts like a dict. It, however, should not be a subclass of dict
    It should support item access, deletion and insertion:
    
    dictionary_obj=Dictionary()
    
    dictionary_obj[key]
    dictionary_obj[key] = item
    del dictionary_obj[key]
    ```
    All keys passed in the test cases are hashable.
    """
    
    def __init__(self):
        raise ChallengeNotAttempted


class JavascriptObject:
    """
    ================================
    Python OOP challenge level 0b100
    ================================
    
    Write a class that acts like a javascript object.
    That is, in addition to all functions described above in Dictionary,
    it supports attribute access as dictionary access and attribute assignment as dictionary insertion.
    All keys given are strings and valid variable names per Python standard.
    
    js_obj=JavascriptObject()

    And these two expressions are equivalent
    
    js_obj["key"]
    js_obj.key
    
    
    For testing purpose, please do not subclass Dictionary even though they share some functionalities.
    Copy and paste the relevant code instead.
    """
    
    def __init__(self):
        raise ChallengeNotAttempted


class ErrorSuppressor:
    """
    ================================
    Python OOP challenge level 0b101
    ================================

    We all hate errors. We all love bug free codes. But sometimes exceptions are what we get to deal with.
    We want to suppress all errors, but we also want to know what happened when necessary.
    Write a **class** that can suppress the error, as context manager, and return the last error when necessary.

    ```
    suppressor = ErrorSuppressor()
    with suppressor:
        print([][1])

    with suppressor:
        print({}['?'])

    with suppressor:
        print(1/0)
    ```
    upon the execution of the above code, four things should happen:
    1. The program continue to run with no error
    2. suppressor.last_error == ZeroDivisionError
    3. suppressor.error_count == 3
    4. suppressor.errors_list == [IndexError, KeyError, ZeroDivisionError]

    Hint: __exit__
    """
    
    def __init__(self):
        raise ChallengeNotAttempted
    

class SingletonWithNew:
    """
    ================================
    Python OOP challenge level 0b110
    ================================
    
    Write a singleton class. That is, the constructor should always return the same object.
    Singleton() is Singleton() should always evaluate to true.
    For this challenge, you should implement it by overriding the __new__ method.
    """
    
    def __new__(cls, *args, **kwargs):
        raise ChallengeNotAttempted


class SingletonWithMeta:
    """
    ================================
    Python OOP challenge level 0b111
    ================================
    
    Again, write a singleton class. However, you should use a metaclass instead of overriding __new__ this time.
    """
    
    def __init__(self):
        raise ChallengeNotAttempted


class SuperDictionary:
    """
    =================================
    Python OOP challenge level 0b1000
    =================================
    
    Wow we have a super dictionary this time. You can access everything inside either on the class
    or on an instance of that class.
    
    It supports all regular (challenge 2) dictionary operations
    
    d=SuperDictionary()
    
    d[key]
    d[key] = item
    del d[key]
    
    For users' convenience, there is no difference whether to access the data on the SuperDictionary,
    or on an instance of the class, as they only ever need one SuperDictionary.
    
    d=SuperDictionary()
    d[key] = item
    d[key] == item
    SuperDictionary[key] == item
    
    It also supports Javascript-like (challenge 3) attribute accessing.
    
    d["key"] == d.key
    
    So, in combination with the feature above, these statements are functionally identical
    
    d["key"] ==  SuperDictionary.key
    d["key"] ==  SuperDictionary["key"]
    d.key == SuperDictionary.key
    d.key == SuperDictionary["key"]
    
    The SuperDictionary also supports attributes assignment.
    This means the following four statements have the same effect
    
    SuperDictionary.key = item
    SuperDictionary().key = item
    SuperDictionary["key"] = item
    SuperDictionary()["key"] = item
    
    Deletions can be done either on the class or the instance as well
    
    del SuperDictionary["key"]
    del SuperDictionary()["key"]

    Some combinations are not completely covered here so you may want to
    look into the test_data_integrity_overall function in test.py
    
    Hint: you may want to start with making the SuperDictionary a singleton
    """
    def __init__(self):
        raise ChallengeNotAttempted
