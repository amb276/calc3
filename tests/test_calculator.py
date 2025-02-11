'''My Calculator Test'''
from calculator import add, multiply, subtract

def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(2,2) == 0

def test_multiplication():
    assert multiply(2,2) == 4

"""def test_division():
    assert divide(2,2) == 1"""

