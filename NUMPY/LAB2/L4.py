"""
Instructions --

You managed to get hold on the changes in weight, height and age of all baseball players. It is available as a 2D Numpy array, update. 
Add np_baseball and update and print out the result.
You want to convert the units of height and weight. As a first step, create a Numpy array with three values: 0.0254, 0.453592 and 1. 
Name this array conversion.
Multiply np_baseball with conversion and print out the result.
"""

# baseball is available as a regular list of lists
# update is available as 2D Numpy array

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and update
print (np_baseball + update)

# Create Numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print (np_baseball * conversion)
