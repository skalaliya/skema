#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:34:10 2023

@author: skalaliya
"""
while(True):
    print("this programe will help you to calcuate your speed", "please provide us the following information to use the programe")
    Name = input("please enter your name:- ")
    Email = input("please enter yor email ID:- ")
    try:
        Distance = int(input("please tell your distance travelled in Kms:- "))
        Time  = int(input("please enter your time travelled in Hrs:- "))
        
        Speed = Distance/Time
        print("your speed is",Speed)
    except Exception as e:
        print("Your error is ",e)