#!/usr/bin/python3


def no_c(my_string):
    another_string = my_string.translate({ord(i): None for i in "Cc"})
    return another_string
