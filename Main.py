# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Nahien Chowdhury, December 3rd, 2019, Assignment 09
# ------------------------------------------------------------------------ #

# 1. Create the Person class in the DataClasses.py file (Listing 6). (Done)
# 2. Modify the TestHarness.py file by adding code to test the Person class (Listing 8). (Done in TestHarness.py)
# 3. Create the Employee class in the DataClasses.py file (Listing 9). (Done)
# 4. Modify the TestHarness.py file by adding code to test the Employee class (Listing 10). (Done in TestHarness.py)
# 5. Create the FileProcessor class in the ProcessingClasses.py file (Listing 7). (Done)
# 6. Modify the TestHarness.py file by adding code to test the FileProcessor class (Listing 10). (Done in TestHarness.py)
# 7. Create the EmployeeIO class in the IOClasses.py file (Listing 11). (Done)
# 8. Modify the TestHarness.py file by adding code to test the EmployeeIO class (Listing 12). (Done in TestHarness.py)

# Objective: Now that the code is tested, you need a main module as the starting point of your application.
# Copy and paste the code in Listing 13 into Main.py. Currently, the code does nothing, but it does include pseudo-code (Listing 1). (Done)
# Your task is to read and understand the pseudo-code, then add code to make the application work. Make sure to include error handling!

#TODO: Import Modules

import DataClasses
import ProcessingClasses
import IOClasses

if __name__=="__main__": # Similar to Listing08, copying foundation to set up importing of modules.
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported") # Error handling from Listing08

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of employee objects (Done)
    # Let user add data to the list of employee objects (Done)
    # let user save current data to file (Done)
    # Let user exit program (Done)

EmployeeTable = []  # Initializing a list table for objects
lstFileData = []    # Initializing a list table for objects

lstFileData = Fp.read_data_from_file("EmployeeData.txt")
for row in lstFileData:
    EmployeeTable.append(Emp(row[0], row[1], row[2].strip()))

# Show user a menu of options
while True:
    Eio.print_menu_items()
    strOption = Eio.input_menu_options()
    if strOption == "1": # Show user current data in the list of employee objects
        Eio.print_current_list_items(EmployeeTable)
        continue
    elif strOption == "2": # Let user add data to the list of employee objects
        EmployeeTable.append(Eio.input_employee_data())
        continue
    elif strOption == "3": # let user save current data to file
        if ("y" == str(input("Save this data to file? (Y / N) - ")).strip().lower()):  # Double-check with user
            Fp.save_data_to_file("EmployeeData.txt", EmployeeTable)
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:  # Let the user know the data was not saved
            input("New data was NOT saved, but previous data still exists. Press the [Enter] key to return to menu.")
            continue
    elif strOption == "4": # Let user exit program
        break