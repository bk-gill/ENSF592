# input_processing.py
# BALKARN GILL, ENSF 592 P23
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 git repository.

class Sensor:
    # Constructor that initializes instance variables
    def __init__(self):
        self.light = "green" # Default value for light variable
        self.vehicle = "no" # Default value for vehicle variable
        self.pedestrian = "no" # Default value for pedestrian variable
        self.action = "Proceed" # Default value for action variable

    # This function inputs which instance variable (light, vehicle, pedestrian) is being changed 
    # and what change is being made to it. The function later uses the changes to compute the action variable.
    def update_status(self): 
        while True: 
            print("Are changes detected in the vision input?")
            try:
                response = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ") # User input that decides where the sensor change is being made
                if response not in ["0","1","2","3"]: # If the user input is not in this list, raise a ValueError
                    raise ValueError
                else: # If the response is in the list above, the control statements below decide which variable is being changed
                    if response == "0": # This control statement is used to end the program if user selects "0"
                        break

                    elif response == "1": # If response is 1, light variable is being changed
                        self.light= input("What change has been identified?: ") # User input to decide what to change light variable to
                        if self.light not in ["green", "yellow", "red"]: # If previous input is not in this list, inform user of invalid entry and reprompt
                            print("\n","Invalid entry, please try again.","\n")
                            continue
                
                    elif response == "2": # If response is 2, pedestrian is being changed 
                        self.pedestrian = input("What change has been identified?: ") # User input to decice what to change pedestrian variable to
                        if self.pedestrian not in ["yes", "no"]: # If previous input is not in this list, inform user of invalid entry and reprompt
                            print("\n","Invalid entry, please try again.","\n") 
                            continue

                    elif response == "3": # If response is 3, vehicle is being changed
                        self.vehicle = input("What change has been identified?: ") # User input to decice what to change vehicle variable to
                        if self.vehicle not in ["yes", "no"]: # If previous input is not in this list, inform user of invalid entry and reprompt
                            print("\n","Invalid entry, please try again.","\n")
                            continue

                    sensor = [self.light, self.pedestrian, self.vehicle] # list including values of light, pedestrian, and vehicle
                    if sensor[0] == "green" and sensor[1]== "no" and sensor[2] == "no": # If corresponding values of variables are equal to this control statement, change action variable to proceed
                        self.action = "Proceed"
                    elif sensor[0] == "yellow" and sensor[1]== "no" and sensor[2] == "no": # If corresponding values of variables are equal to this control statement, change action variable to caution
                        self.action = "Caution"
                    else: # For any other combinations, change action variable to stop
                        self.action = "STOP" 

                    print_message(self) # Calls the print_message function

            except ValueError as err: # In the case that ValueError is raised, inform user of invalid entry and reprompt
                print("\n","Invalid selection. Please try again.", "\n")

# This function passes the sensor object and prints the action message and current status. Values are called from the Sensor class.
def print_message(sensor):
    action = sensor.action
    print("\n",action,"\n")
    print("Light = ", sensor.light, ",","Pedestrian = ", sensor.pedestrian, ",", "Vehicle = ", sensor.vehicle,"\n")

# Main function calls the update_status function and passes the Sensor class as an argument 
def main():
    print("\n***ENSF 592 Car Vision Detector Processing Program***\n")
    sensor = Sensor()
    sensor.update_status()

# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()
