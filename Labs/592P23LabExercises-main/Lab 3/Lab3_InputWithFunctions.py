# ENSF 592 Spring 2023
# May 11 Lab 3
# Input With Functions (continued from Lab 2)

# Add comments to explain the functionality of this program


def get_user_input(n):
    entry = input("Please type any entry #" + str(n + 1) + ": ")
    return entry, type(entry)

def process_user_input(n, entry, type):
    print("This is entry #" + str(n + 1) + ":", entry)
    print("The type of entry #" + str(n + 1) + " is :", str(type))


# Input Method 3
print('\n' * 2)
print("***METHOD 3***")
num_of_repeats = 3
results = []
results_types = []

for i in range(num_of_repeats):
    a, b = get_user_input(i)
    results.append(a)
    results_types.append(b)

for i in range(num_of_repeats):
    process_user_input(i,results[i], results_types[i])

