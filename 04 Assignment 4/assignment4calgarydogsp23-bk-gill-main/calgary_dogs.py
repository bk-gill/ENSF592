# calgary_dogs.py
# Balkarn Gill
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

# Import necessary libraries
import numpy as np
import pandas as pd

def main():
    # Read data from an excel file and select only the columns from 0 to 3
    all_data = pd.read_excel(r"./CalgaryDogBreeds.xlsx", usecols=[0, 1, 2, 3])
    # Set multi-level index ('Year', 'Month', 'Breed') for the dataframe
    all_data.set_index(['Year', 'Month', 'Breed'], inplace=True)

    print("ENSF 592 Dogs of Calgary")

    # Loop until the user inputs a breed that exists in the data
    while True:
        input2 = input("Enter a dog breed: ")
        try:
            # Try to get the data for the breed specified by the user
            breed_data = all_data.loc[pd.IndexSlice[:, :, input2.upper()], :]
            break
        except KeyError:
            # If breed doesn't exist in the data, print an error message
            print("Dog breed not found in the data. Please try again.")

    # Get the unique years in which the breed appears in the data
    year_mask = breed_data.index.get_level_values('Year').unique()
    print(f"The {input2.upper()} was found in the top breeds for years: ", *year_mask)

    # Calculate the sum of 'Total' registrations for the input breed
    total_registrations = breed_data['Total'].sum()
    print(f"There have been {total_registrations} {input2.upper()} dogs registered total.")

    # Calculate the sum of registrations for the breed by year
    breed_totals_per_year = breed_data.groupby('Year')['Total'].sum()

    # Calculate the breed's percentage of top breeds for each year
    for year in year_mask:
        breed_total = breed_totals_per_year[year]
        year_total = all_data.loc[year].sum().values[0]
        percentage = (breed_total / year_total) * 100
        print(f"The {input2.upper()} was {percentage:.6f}% of top breeds in {year}.")

    # If the breed wasn't in the top breeds for 2023, explicitly state it
    if 2023 not in year_mask:
        print(f"The {input2.upper()} was 0.0% of top breeds in 2023.")

    # Calculate the breed's percentage of top breeds across all years
    three_year_total = all_data.loc[pd.IndexSlice[year_mask, :, :], 'Total'].sum()
    percentage = (total_registrations / three_year_total) * 100
    print(f"The {input2.upper()} was {percentage:.6f}% of top breeds across all years.")

    # Calculate the average number of registrations per month for the breed
    monthly_average = breed_data['Total'].mean()
    rounded_average = int(monthly_average)

    # Find the month(s) in which the breed had the highest number of registrations
    month_counts = breed_data.groupby(level='Month').size()
    max_count = month_counts.max()
    highest_months = month_counts[month_counts == max_count].index
    print(f"Most popular month(s) for {input2.upper()} dogs:", ', '.join(highest_months))

# Execute the main function if the script is run directly
if __name__ == '__main__':
    main()