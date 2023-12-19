# ENSF 592 Spring 2023
# May 30 Lab 8
# Exercises
 
import numpy as np
import pandas as pd

# Refer to the weather data stored in WeatherData.xlsx


# Demo: creating/exporting a multi-dimensional DataFrame from Excel

all_data = pd.read_excel(r".\WeatherData.xlsx", usecols = [2,5,6,7,8,9,10], index_col = [0,1,2,3])
#all_data.to_excel(r".\WeatherExport.xlsx", index = True, header = True)

#print(all_data.index)

# Add a column to calculate the delta for day (difference between max and min)

all_data["Delta"] = all_data["Max Temp (°C)"] - all_data["Min Temp (°C)"]
print(all_data)

# Find the average measurements for each month (across both years)

print(all_data.groupby(level="Month").mean())

# Print the data in both locations on May 1, 2021

print(all_data.loc[:,2021,5,1])

