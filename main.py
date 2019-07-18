# -*- coding: utf-8 -*-

def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5

def sum(x, y):
    return x + y + 1

def simple_unittest_sum():
    assert sum(3, 3) == 6, "should be 6"

if __name__ == "__main__":
    simple_unittest_sum()
    print("Everything is passed")
