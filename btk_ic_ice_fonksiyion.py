# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 11:49:21 2022

@author: tosun
"""

#us_alma
def usalma(number):
    def inner(power):
        return number**power
    return inner
two = usalma(3)
print(two(3))

