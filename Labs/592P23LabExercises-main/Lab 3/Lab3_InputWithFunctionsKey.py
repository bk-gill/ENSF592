# ENSF 592 Spring 2023
# May 11 Lab 3
# Input With Functions (continued from Lab 2)

# Add comments to explain the functionality of this program


# get_user_input prompts for any input entry and returns the input value and its type
# Argument: Takes in a number to count which input prompt is being given
# Returns the input value (str object) and its corresponding type (type object)
def get_user_input(n):
    entry = input("Please type any entry #" + str(n + 1) + ": ")
    #print(type(entry))             # Uncomment this line to observe the internal process
    #print(type(type(entry)))       # Uncomment this line to observe the internal process
    return entry, type(entry)

# process_user_input prints a value that was previously input and its type
# Argument: Takes in a number to count which input prompt is being printed, the original input value, and the type of the value
# No return value
def process_user_input(n, entry, type):
    print("This is entry #" + str(n + 1) + ":", entry)
    print("The type of entry #" + str(n + 1) + " is :", str(type))


# Input Method 3
print('\n' * 2) # Add header for spacing
print("***METHOD 3***")
num_of_repeats = 3  # set number of inputs to prompt for
results = [] # create empty list to store inputs
results_types = [] # create list for types

# Call get_user_input three times, add values to the list for input and its corresponding type
for i in range(num_of_repeats):
    a, b = get_user_input(i)
    results.append(a)
    results_types.append(b)

# Call process_user_input, pass input counter, the actual input, and the type of that input
for i in range(num_of_repeats):
    process_user_input(i,results[i], results_types[i])


