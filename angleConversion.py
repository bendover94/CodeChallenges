#1. Convert radians into degrees
#Write a function in Python that accepts one numeric parameter. 
#This parameter will be the measure of an angle in radians. 
#The function should convert the radians into degrees and then return that value.
#While you might find a Python library to do this for you, you should write the function yourself. 
#One hint you get is that you'll need to use Pi in order to solve this problem. 
#You can import the value for Pi from Python's math module. #math.pi

# rad -> Grad: x/pi*180

import math

def rad2degree(rad_input):
    print(rad_input / math.pi * 180)

rad2degree(2 * math.pi)
