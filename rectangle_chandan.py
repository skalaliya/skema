#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:21:20 2023

@author: skalaliya
"""

def rectangle():
    """
    This function prompts the user to enter the length and breadth of a rectangle,
    then calculates and prints the area and perimeter of the rectangle.
    """
    try:
        length = float(input("Enter the length of the rectangle: "))
        breadth = float(input("Enter the breadth of the rectangle: "))
        
        # Calculate area
        area = length * breadth
        
        # Calculate perimeter
        perimeter = 2 * (length + breadth)
        
        # Print the results
        print(f"The area of the rectangle is {area} square units.")
        print(f"The perimeter of the rectangle is {perimeter} units.")
    
    except ValueError:
        print("Invalid input! Please enter numerical values for length and breadth.")

# Call the rectangle function
if __name__ == "__main__":
    rectangle()
