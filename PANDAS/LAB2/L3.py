"""
Instructions --

Use single square brackets to print out the country column of cars as a Pandas Series.
Use double square brackets to print out the country column of cars as a Pandas DataFrame. Do this by putting country in two square 
brackets this time.
"""

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print (cars['country'])

# Print out country column as Pandas DataFrame
print (cars[['country']])
