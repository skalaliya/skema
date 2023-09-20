#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:21:20 2023

@author: skalaliya
"""

def ractangle():
    l = int(input("length: "))
    b = int(input("breadth: "))
    area = l*b
    p = 2*(l+b)
    return print("area of a ractangle is ", area,"and the parimeter is ", p)


ractangle()