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
# If you leave this in while also printing plots below, just close the first set of figures and then the rest of the code will continue.
# plt.show() is a "blocking function" - the rest of the code will not execute until the windows are closed.



# More practice for Quiz 2/Project

# Import the weather data from WeatherPractice.xlsx. There are two different sheets and they are slightly different than previously seen.
# Merge based on Climate ID and delete any duplicate columns. 

measurements = pd.read_excel("WeatherPractice.xlsx", sheet_name = 'Measurements')
coordinates = pd.read_excel("WeatherPractice.xlsx", sheet_name = 'Coordinates')
weather_data = pd.merge(measurements, coordinates, on = 'Climate ID').drop('Name', axis = 1)

print('\nMERGED DATA\n')
print(weather_data.head())

# Use a regular expression to find the rows where the month ends in "ary".

print('\nREGULAR EXPRESSION RESULTS\n')
print(weather_data['Month'].str.findall(r'.*ary$'))
print(weather_data['Month'].str.extract(r'(.*ary$)'))
# Both will work in this case!

# Set a hierarchical index in the order of Station Name -> Year -> Month -> Day. Sort the data in order of the index.

print('\nINDEXED AND SORTED\n')
weather_data = weather_data.set_index(['Station Name', 'Year', 'Month', 'Day']).sort_index()
print(weather_data.head())

# Add a column to show the change in temperature for each day.

print('\nDELTA COLUMN ADDED\n')
weather_data['Temp Delta'] = weather_data['Max Temp (°C)'] - weather_data['Min Temp (°C)']
print(weather_data.head())

# Use your knowledge of Pandas to find the average maximum and minimum temperatures for each month.
# Try using both groupby and pivot tables.
# Create a plot to show everything on the same graph.
# Then try plotting each station on a separate subplot.

# Method 1: Using groupby

avg_group = weather_data.groupby(['Month', 'Station Name'])[['Max Temp (°C)', 'Min Temp (°C)']].mean().unstack()  
# You don't need to unstack, but it displays the results more clearly and is easier for plotting.
# This is an example of why pivot tables can be easier to work with than groupby.
# If you only use one set of square brackets around Max/Min, you'll get a deprecation warning. Both syntax versions will work (for now), but it's better to pass multiple columns as a list.
print("\nGROUPBY\n")
print(avg_group)

# Plot everything together
plt.figure(4)       # Specifying a figure number of each plot can help avoid overlaps in setting axes, labels, etc.
plt.plot(avg_group) # You can also assign the result to a variable and then use that variable to call the methods (see subplots for an example)
plt.title('Station Temperature Measurements')
plt.xlabel('Month')
plt.ylabel('Temp (°C)')
plt.legend(['Max Temp (°C) at CALGARY INTL A', 'Max Temp (°C) at CALGARY SPRINGBANK A', 'Min Temp (°C) at CALGARY INTL A', 'Min Temp (°C) at CALGARY SPRINGBANK A'])

# Plot using subplots
station_compare = plt.figure(5)
(top, bottom) = station_compare.subplots(2)
station_compare.suptitle('Comparison by Station')
top.plot(avg_group.loc[:,pd.IndexSlice[:,'CALGARY INTL A']])    # Use an IndexSlice to access the multi-level columns.
bottom.plot(avg_group.loc[:,pd.IndexSlice[:,'CALGARY SPRINGBANK A']])    # Use an IndexSlice to access the multi-level columns.
top.set(xlabel = 'Month', ylabel = 'Temp (°C)')
bottom.set(xlabel = 'Month', ylabel = 'Temp (°C)')
top.set_title('Data for CALGARY INTL A')
bottom.set_title('Data for CALGARY SPRINGBANK A')
top.legend(['Max Temp (°C)', 'Min Temp (°C)'])
bottom.legend(['Max Temp (°C)', 'Min Temp (°C)'])


# Method 2: Using pivot tables

avg_data = weather_data.pivot_table(index = 'Month', columns = 'Station Name', aggfunc = {'Max Temp (°C)':'mean', 'Min Temp (°C)':'mean'})
print("\nPIVOT TABLE\n")
print(avg_data)

# Plot everything together
plt.figure(6)       # Same as above
plt.plot(avg_data)
plt.title('Station Temperature Measurements')
plt.xlabel('Month')
plt.ylabel('Temp (°C)')
plt.legend(['Max Temp (°C) at CALGARY INTL A', 'Max Temp (°C) at CALGARY SPRINGBANK A', 'Min Temp (°C) at CALGARY INTL A', 'Min Temp (°C) at CALGARY SPRINGBANK A'])

# Plot using subplots
plt.figure(7)   # Same as above
station_compare_pvt = plt.figure(7)
(top, bottom) = station_compare_pvt.subplots(2)
station_compare_pvt.suptitle('Comparison by Station')
top.plot(avg_data.loc[:,pd.IndexSlice[:,'CALGARY INTL A']])    # Use an IndexSlice to access the multi-level columns.
bottom.plot(avg_data.loc[:,pd.IndexSlice[:,'CALGARY SPRINGBANK A']])    # Use an IndexSlice to access the multi-level columns.
top.set(xlabel = 'Month', ylabel = 'Temp (°C)')
bottom.set(xlabel = 'Month', ylabel = 'Temp (°C)')
top.set_title('Data for CALGARY INTL A')
bottom.set_title('Data for CALGARY SPRINGBANK A')
top.legend(['Max Temp (°C)', 'Min Temp (°C)'])
bottom.legend(['Max Temp (°C)', 'Min Temp (°C)'])


plt.show()  # Only need once - comment out the one above in the lab examples. 
# If you leave the upper show() in, just close the first set of figures and then the rest of the code will continue.


# Bonus: Create and print a set of the month names. 
# You'll need to access the index values themselves using the Index object.
# I won't ask this on the quiz, it's just an interesting bit of code to try.

months = weather_data.index.get_level_values(2).values
print(set(months))
