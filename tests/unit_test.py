# Tanner Hess
# tmh648
# Software Testing Q & A: Assignment 3

import pytest
from app.BMI_calc import *

'''
This file splits up the test cases into 4 catgeories:
1) Underweight
2) Normal
3) Overweight
4) Obese

Each of these categories have a designated test function parametrized to test the 5 test
cases for each one (3 test cases for Obese as there is no upper limit).

** Note that the parametrization holds 4 values: the test number, the height in inches and
feet, and the pounds all to achieve the desired BMI listed in the comment above the parameter.
'''



# Test points include: 0, 0.1, 12, 18.4, 18.5  -->                  0.0             0.1           12             18.4            18.5
@pytest.mark.parametrize('test_number, feet, inches, pounds', [(1, 15, 0, 1), (2, 10, 0, 1), (3, 5, 0, 60), (4, 5, 5, 108), (5, 5, 4, 105)])
def test_under(test_number, feet, inches, pounds):
    if test_number == 1:
        assert BMI(feet, inches, pounds)[1] == "Error"
    elif test_number == 2:
        assert BMI(feet, inches, pounds)[1] == 'Underweight'
    elif test_number == 3:
        assert BMI(feet, inches, pounds)[1] == 'Underweight'
    elif test_number == 4:
        assert BMI(feet, inches, pounds)[1] == 'Underweight'
    elif test_number == 5:
        assert BMI(feet, inches, pounds)[1] == 'Normal'
    else:
        print("Error, invalid test case!")


# Test points include: 18.4, 18.5, 21, 24.9, 25  -->                18.4           18.5            21             24.9             25
@pytest.mark.parametrize('test_number, feet, inches, pounds', [(1, 5, 5, 108), (2, 5,4,105), (3, 5, 5, 123), (4, 5, 5, 146), (5, 5, 4, 142)])
def test_normal(test_number, feet, inches, pounds):
    if test_number == 1:
        assert BMI(feet, inches, pounds)[1] == 'Underweight'
    elif test_number == 2:
        assert BMI(feet, inches, pounds)[1] == 'Normal'
    elif test_number == 3:
        assert BMI(feet, inches, pounds)[1] == 'Normal'
    elif test_number == 4:
        assert BMI(feet, inches, pounds)[1] == 'Normal'
    elif test_number == 5:
        assert BMI(feet, inches, pounds)[1] == 'Overweight'
    else:
        print("Error, invalid test case!")


# Test points include: 24,9, 25, 28, 29.9, 30  -->                  24.9            25              28              29.9            30
@pytest.mark.parametrize('test_number, feet, inches, pounds', [(1, 5, 5, 146), (2, 5, 4, 142), (3, 5, 0, 140), (4, 6, 0, 215), (5, 5, 5, 176)])
def test_over(test_number, feet, inches, pounds):
    if test_number == 1:
        assert BMI(feet, inches, pounds)[1] == 'Normal'
    elif test_number == 2:
        assert BMI(feet, inches, pounds)[1] == 'Overweight'
    elif test_number == 3:
        assert BMI(feet, inches, pounds)[1] == 'Overweight'
    elif test_number == 4:
        assert BMI(feet, inches, pounds)[1] == 'Overweight'
    elif test_number == 5:
        assert BMI(feet, inches, pounds)[1] == 'Obese'
    else:
        print("Error, invalid test case!")


# Test points include: 29.9, 30, 50 ...
#  only 3 cases needed as no upper boundary: Obese = [30, inf) -->  29.9            30            50
@pytest.mark.parametrize('test_number, feet, inches, pounds', [(1, 6, 0, 215), (2, 5, 5, 176), (3, 5, 0, 250)])
def test_obese(test_number, feet, inches, pounds):
    if test_number == 1:
        assert BMI(feet, inches, pounds)[1] == 'Overweight'
    elif test_number == 2:
        assert BMI(feet, inches, pounds)[1] == 'Obese'
    elif test_number == 3:
        assert BMI(feet, inches, pounds)[1] == 'Obese'
    else:
        print("Error, invalid test case!")
