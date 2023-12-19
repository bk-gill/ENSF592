# ENSF 592 Spring 2023
# May 18 Lab 5
# Exercises for Quiz 1 Review - Solutions

# Solve the exercises provided in main.

# Some documentation is included as an example (in mostly Google Style). The documentation is not complete!
# All methods should have their own docstrings unless otherwise specified (i.e. __init__ and  properties)
# The specifics of other formats may vary- you may choose whichever format you prefer as long as you are consistent.

import re

class Horse:
    """A class used to create Horse object.

        Attributes:
            name (str): String that represents the horse's name
            age (int): Integer that represents the horse's age
            colour (str): String that represents the horse's colour
            breed (str): String that represents the horse's breed
            ***Note that self is implicit and is not included!

    """

    sci_name = "Equus caballus"
    """sci_name (str): Class variable with default string value of "Equus caballus"
    """

    def __init__(self, name, age, colour, breed):
        self.__name = name 
        self.__age = age
        self.__colour = colour
        self.__breed = breed


    # Define all private instance variables as properties to get getters/setters
    @property #decorator
    def name(self):
        return self.__name

    @property #decorator
    def colour(self):
        return self.__colour

    @property #decorator
    def age(self):
        return self.__age

    @property #decorator
    def breed(self):
        return self.__breed

    # Define any customized getters/setters
    @age.setter
    def age(self, new_val):
        try:
            if new_val <= 0:
                raise ValueError()
            else:
                self.__age = new_val
                print("Happy birthday!")
        except ValueError:
            print("Age must be greater than 0.")

    # Define instance methods
    def print_all_stats(self):
        print("""{0} stats: Age = {1}, Colour = {2}, Breed = {3}.""".format(self.name, self.age, self.colour, self.breed))

    # Define class methods
    @classmethod
    def horse_info(cls):
        print("The scientific name of a horse is: " + cls.sci_name)


class Rider:
    
    def __init__(self, name, age, horse):
        self.name = name
        self.age = age
        self.horse = horse

    def print_all_stats(self):
        print("""{0} stats: Age = {1}, Horse Age = {2}, Horse Colour = {3}, Horse Breed = {4}."""
        .format(self.name, str(self.age), str(self.horse.age), self.horse.colour, self.horse.breed))        



# Generator functions can be used for various scenarios instead of repeating the expressions
# This version yield each value as a string
def comp_ages_string(list_objects, min, max):
    for current_object in list_objects:
        if current_object.age + 5 > min and current_object.age + 5 < max:
            yield current_object.name


# This version will yield the results as a list
def comp_ages_list(list_objects, min, max):
    final_results = []
    for current_object in list_objects:
        if current_object.age + 5 > min and current_object.age + 5 < max:
            final_results.append(current_object.name)

    yield final_results


def main():
    print("\n***Horse and Rider Program***\n")


    # Create five horses and five riders.
    horse1 = Horse("Blaze", 14, "bay", "Morgan")
    horse2 = Horse("Socks", 9, "grey", "Arabian")
    horse3 = Horse("Thunder", 20, "black", "Friesian")
    horse4 = Horse("Lightning", 14, "brown", "Quarter Horse")
    horse5 = Horse("Harry", 11, "grey", "Quarter Horse")

    rider1 = Rider("Alex", 34, horse1)
    rider2 = Rider("Jordan", 45, horse2)
    rider3 = Rider("Ali", 28, horse3)
    rider4 = Rider("Page", 20, horse4)
    rider5 = Rider("Jay", 14, horse5)

    # Exercise 1
    # Collect all horse and rider ages and create a single set that lists each number that appears at least once.
    # A large competition is planned for 5 years from now. All riders must be over 20, but under 50. Horses must be over 10 and under 25.
    # Create either a single generator function or separate generator expressions that can be used to find which horses and riders will be eligible for the competition.
    # Print out their names.

    horses = [horse1, horse2, horse3, horse4, horse5]
    riders = [rider1, rider2, rider3, rider4, rider5]

    # You can iterate over objects in a list
    horse_ages = [n.age for n in horses]
    rider_ages = [n.age for n in riders]

    # Or access the variables contained within each object
    age_set = set([horses[n].age for n in range(len(horses))] + [riders[n].age for n in range(len(riders))])
    print("Set of ages: ", age_set)

    # Generator expressions (same options - iterating over the objects or their variables)
    comp_horses = (n.name for n in horses if n.age + 5 > 10 and n.age + 5 < 25)
    comp_riders = (riders[n].name for n in range(len(riders)) if riders[n].age + 5 > 20 and riders[n].age + 5 < 50)
    comp_name = [*comp_horses, *comp_riders]
    print("Competition names: ", comp_name)

    # Generator functions can be used to find the generator expression for both types of objects
    print("Competition horse names: ", *comp_ages_string(horses, 10, 25))
    print("Competition rider names: ", *comp_ages_string(riders, 20, 50))
    print("Competition horse names in a list: ", *comp_ages_list(horses, 10, 25))
    print("Competition rider names in a list: ", *comp_ages_list(riders, 20, 50))
    

    # Exercise 2
    # Use a regular expression to find all competition-eligible horses and riders with names containing both "A/a" and "L/l"

    comp_str = " ".join(comp_name)
    # regex = re.compile('\w*[ALal]\w*[ALal]\w*')  ### Works for these cases, but will also find names with two ls and two as instead of one of each.
    # found = regex.findall(comp_str)

    regex = re.compile('\w*[Aa]\w*')  # find all names containing 'a' first
    containing_a = regex.findall(comp_str)
    regex = re.compile('\w*[Ll]\w*')  # then check to see if they also contain 'l'
    containing_a_l = regex.findall(" ".join(list(containing_a)))
    print("Names found to contain both A/a and L/l: ", *containing_a_l)
    # ***Note: a lookahead assertion could also be used, but that is a more advanced application of regular expressions


    # Exercise 3:
    # Customize the setter for horse age by adding an exception. 
    # Age must be set to a value greater than zero, otherwise a message is printed to the user using a ValueError exception.
    print("Changing age of Blaze...")
    horse1.age = 15
    horse1.print_all_stats()

    print("Changing age of Socks...")
    horse2.age = 0
    horse2.print_all_stats()



    # Want some additional practice? Try the following.

    # Practice 1:
    # Customize the setter for the rider's name so that only letters from A-Z/a-z are accepted.
    # Test result: A name such as Kesha should be valid, a name such as Ke$ha should throw an error.

    # Practice 2:
    # Use a regular expression to find all horse breeds that end with "an".
    # Test result: Morgan, Arabian, Friesian

    # Practice 3:
    # Construct a single set that lists all unique horse colours.
    # Test result: bay, grey, black, brown

    # Practice 4:
    # Create both a generator expression and its equivalent generator function that can be used to calculate how old each rider will be in 2031.
    # Create tuples to pair each rider with their future age. Print out the results.
    # Test result: (Alex, 44) (Jordan, 55) (Ali, 38) (Page, 30) (Jay, 24)

    # Practice 5:
    # Create a dictionary where the rider's name is the key and their assigned horse is the value. Use the dictionary to find and print the name of Ali's horse.
    # Test result: Thunder


if __name__ == '__main__':  # optional in Python 3
    main()


