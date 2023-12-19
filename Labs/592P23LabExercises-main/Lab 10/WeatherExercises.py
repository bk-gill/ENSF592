# ENSF 592 Spring 2023
# June 6 Matplotlib Demo and Practice Exercises
 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Refer to the weather data stored in WeatherDataPlotting.xlsx

# Demo: examples of Matplotlib output

data = pd.read_excel("WeatherDataPlotting.xlsx", usecols = [2,4,8,9,10])
data.sort_index()


# Create a pivot table to map station name vs. date-time for all mean temp measurements

select_data = data.pivot_table('Mean Temp (°C)', index = 'Date/Time', columns = 'Station Name')
print(select_data)

#FIGURE 1
plt.plot(select_data) # Passes the data to the plotting method


# Create a DatetimeIndex object to easily search by Year, Month, Day

date_index = pd.to_datetime(data['Date/Time'].values)
print(date_index)
select_data = data.pivot_table('Mean Temp (°C)', index = date_index, columns = 'Station Name')
print(select_data)

#FIGURE 2
select_data.plot()  # Calling from the data itself will giving you the legend automatically


# Let's make it prettier...
# FIGURE 3
year_compare, (top, bottom) = plt.subplots(2)    # Create two subplots to compare years
year_compare.suptitle('Comparison by Year')     # Add the top title
top.plot(select_data.loc['2020'])   # Add data to top subplot
bottom.plot(select_data.loc['2021'])   # Add data to next subplot

# Now add labels and subplot titles
top.set(xlabel = 'Date', ylabel = 'Mean Temp (°C)') 
bottom.set(xlabel = 'Date', ylabel = 'Mean Temp (°C)')
top.set_title('Data for 2020')
bottom.set_title('Data for 2021')

# Automatically set the legend based on the columns
top.legend(['CALGARY INTL A','CALGARY SPRINGBANK A'])
bottom.legend(['CALGARY INTL A','CALGARY SPRINGBANK A'])


plt.show()  # Only need once! Usually at the end of the script.



# More practice for Quiz 2/Project

# Import the weather data from WeatherPractice.xlsx. There are two different sheets and they are slightly different than previously seen.
# Merge based on Climate ID and delete any duplicate columns. 


# Use a regular expression to find the rows where the month ends in "ary".


# Set a hierarchical index in the order of Station Name -> Year -> Month -> Day. Sort the data in order of the index.


# Add a column to show the change in temperature for each day.


# Use your knowledge of Pandas to find the average maximum and minimum temperatures for each month.
# Try using both groupby and pivot tables.
# Create a plot to show everything on the same graph.
# Then try plotting each station on a separate subplot.

# Method 1: Using groupby


# Method 2: Using pivot tables


#plt.show()  # Only need once - comment out the one above in the lab examples when using this one



# Bonus: Create and print a set of the month names. 
# You'll need to access the index values themselves using the Index object.
# I won't ask this on the quiz, it's just an interesting bit of code to try.

