# school_data.py
# Balkarn Gill 
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 3 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

# Import numpy
import numpy as np

# Import data from 2013 to 2022 from the given_data.py file
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Store the raw data in a tuple
raw_data = year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Reshape the raw data into a 3-dimensional NumPy array
reshaped_data_array = np.reshape(raw_data, (10, 20, 3))

# Define a dictionary mapping school codes to school names
school_dict = {
    "1224": "Centennial High School",
    "1679": "Robert Thirsk School",
    "9626": "Louise Dean School",
    "9806": "Queen Elizabeth High School",
    "9813": "Forest Lawn High School",
    "9815": "Crescent Heights High School",
    "9816": "Western Canada High School",
    "9823": "Central Memorial High School",
    "9825": "James Fowler High School",
    "9826": "Ernest Manning High School",
    "9829": "William Aberhart High School",
    "9830": "National Sport School",
    "9836": "Henry Wise Wood High School",
    "9847": "Bowness High School",
    "9850": "Lord Beaverbrook High School",
    "9856": "Jack James High School",
    "9857": "Sir Winston Churchill High School",
    "9858": "Dr. E. P. Scarlett High School",
    "9860": "John G Diefenbaker High School",
    "9865": "Lester B. Pearson High School"
}

# Extract the keys and values from the school dictionary
school_code_list = list(school_dict.keys())
school_name_list = list(school_dict.values())

def main():
    """
    Main function for the school enrollment statistics application. This function takes a user input, checks if 
    it is a valid input by confirming if it's a valid school name or code. It then prints out various
    statistics about that school by extracting data from the given_data.py file using various numpy methods.
    """
    print("\nENSF 592 School Enrollment Statistics")

    # Print Stage 1 requirements here
    print("Shape of full data array: ", reshaped_data_array.shape)
    print("Dimensions of full data array: ", reshaped_data_array.ndim)
    
    # Loop that prompts for user input and checks if it's valid. Raises ValueError and reprompts if input is invalid.
    while True:
        try:
            # Prompt for user input
            school_input = input("Please enter the high school name or school code: ")

            # Check if the input is valid. If the input is not a value in the keys/values of the dictionary school_dict, input is invalid.
            if school_input not in school_dict and school_input not in school_name_list: # If user input is not in the keys or values of the dictionary, raise an error.
                raise ValueError
        
            else: # Otherwise, input provided is valid. Next step is to check if input is school name or code.
                if school_input in school_dict: # If input is in the dictionary keys, it is the code being provided. Must find corresponding name.
                    # Print the school name and code
                    print("\n***Requested School Statistics***")
                    print("\nSchool name: {},".format(school_dict[school_input]), "School Code:", school_input)
                    break

                else: # Otherwise, it is the school name being provided, must find school code using indexing.
                    # Print the school name and code
                    print("\n***Requested School Statistics***")
                    print("\nSchool name: {},".format(school_input), "School Code:", school_code_list[school_name_list.index(school_input)])
                    break

        # This message is printing when ValueError is raised. Prompts user to try again with a valid input.
        except ValueError: 
            print("\nYou must enter a valid school name or code.\n")

    # Get the index of the selected school. The index of name will be equal to the index of the code.
    index = 0 
    if school_input in school_dict: # If user input is in keys value of school_dict, it is the code being provided and index of that code is found.
        index = school_code_list.index(school_input)

    else: # Otherwise, it is the name being provided. Index is found using the list of school names.
        index = school_name_list.index(school_input)

    # Print various statistics based on the selected school (State 2 requirements). 
    # Built in nanmean, nanmax, nanmin, and nansum are used to compute the necessary values without taking into account the NaN values.
    # Compute and print the mean enrollment for Grade 10
    print("Mean enrollment for Grade 10: ", int(np.nanmean(reshaped_data_array[:, index, 0])))

    # Compute and print the mean enrollment for Grade 11
    print("Mean enrollment for Grade 11: ", int(np.nanmean(reshaped_data_array[:, index, 1])))

    # Compute and print the mean enrollment for Grade 12
    print("Mean enrollment for Grade 12: ", int(np.nanmean(reshaped_data_array[:, index, 2])))

    # Compute and print the highest enrollment for a single grade
    print("Highest enrollment for a single grade: ", int(np.nanmax(reshaped_data_array[:, index, :])))

    # Compute and print the lowest enrollment for a single grade
    print("Lowest enrollment for a single grade: ", int(np.nanmin(reshaped_data_array[:, index, :])))

    # Compute and print the total enrollment for each year
    print("Total enrollment for 2013: ", int(np.nansum(reshaped_data_array[0, index, :])))
    print("Total enrollment for 2014: ", int(np.nansum(reshaped_data_array[1, index, :])))
    print("Total enrollment for 2015: ", int(np.nansum(reshaped_data_array[2, index, :])))
    print("Total enrollment for 2016: ", int(np.nansum(reshaped_data_array[3, index, :])))
    print("Total enrollment for 2017: ", int(np.nansum(reshaped_data_array[4, index, :])))
    print("Total enrollment for 2018: ", int(np.nansum(reshaped_data_array[5, index, :])))
    print("Total enrollment for 2019: ", int(np.nansum(reshaped_data_array[6, index, :])))
    print("Total enrollment for 2020: ", int(np.nansum(reshaped_data_array[7, index, :])))
    print("Total enrollment for 2021: ", int(np.nansum(reshaped_data_array[8, index, :])))
    print("Total enrollment for 2022: ", int(np.nansum(reshaped_data_array[9, index, :])))

    # Compute and print the total ten-year enrollment
    print("Total ten-year enrollment: ", int(np.nansum(reshaped_data_array[:, index, :])))

    # Compute and print the mean total enrollment over 10 years
    print("Mean total enrollment over 10 years:", int(np.nansum(reshaped_data_array[:, index, :])/10))

    # Filtering NaN values and setting them to 0
    array_without_nan_values = np.where(np.isnan(reshaped_data_array), 0, reshaped_data_array)

    # Mask the data array where enrollment is less than 500
    array_of_enrollments_over_500 = np.ma.masked_where(array_without_nan_values < 500, array_without_nan_values)

    # Get the compressed array
    compressed_array = array_of_enrollments_over_500[:, index, :].compressed()

    # If the compressed array isn't empty, calculate the median
    if len(compressed_array) > 0:
        median_value = int(np.nanmedian(compressed_array))
        print("For all enrollments over 500, the median value was: ", median_value)

    else: # Otherwise, compressed array is empty because there are no enrollments over 500
        print("No enrollments over 500.")

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")

    # Compute and print the mean enrollment in 2013
    print("Mean enrollment in 2013: ", int(np.nanmean(reshaped_data_array[0, :, :])))

    # Compute and print the mean enrollment in 2022
    print("Mean enrollment in 2022: ", int(np.nanmean(reshaped_data_array[9, :, :])))

    # Compute and print the total graduating class of 2022
    print("Total graduating class of 2022: ", int(np.nansum(reshaped_data_array[9, :, 2])))

    # Compute and print the highest enrollment for a single grade across all years
    print("Highest enrollment for a single grade: ", int(np.nanmax(reshaped_data_array[:, :, :])))

    # Compute and print the lowest enrollment for a single grade across all years
    print("Lowest enrollment for a single grade: ", int(np.nanmin(reshaped_data_array[:, :, :])))

if __name__ == '__main__':
    main()