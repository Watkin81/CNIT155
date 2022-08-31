#====================================================================================
# Jake Watkins, Thursday 11:30am
# Watkin81@purdue.edu
# This Lab Uses ValueError to Obtain Valid User Inputs, as well as using Functions
# and Loops to Convert and Print Information.
#
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#====================================================================================

# Import Math
import math

# Define the Header
def Header():
    print("*******************************************")
    print("*                CNIT155 Lab 9            *")
    print("*                                         *")
    print("*          Steps to Miles Calculator      *")
    print("*******************************************")
    Space()
    
# Since I need line spaces in this program, this will save time
def Space():
    print("")

# Covert Steps to Miles with a Ratio of 1:2000
def StepsToMiles(lst):
    walked_miles = []
    miles = [i / 2000 for i in lst]
    return miles

# Define Main Function
def Main():
        
    # Run the Header code so it displays at the top
    Header()
    
    # Create the Variables and Lists
    count = 1
    lst = []
    
    # Get the User's Input with ValueError Protection Against Invalid Values
    while (len(lst) < 7):
        try:
            steps = int(input("Enter the Number of Steps for Day " + str(count) + ": "))
            if (steps < 0):
                raise ValueError
            else:
                lst.append(steps)
                count = count + 1
        except ValueError:
            Space()
            print("Exception: Wrong Value Entered.")
            print("Please Enter an Integer Value in a Correct Format!\n")
    
    # Convert Steps To Miles
    miles_walked = StepsToMiles(lst)
    Space()
    print("*** The Number of Miles you Walked This Week ***")
    
    # Print the Conversions
    j = 0
    while j < 7:
        print("Day " + str(j+1) + ": " + "{:0.2f}".format(miles_walked[j]) + " Miles")
        j = j + 1
    
    
    # Calculate and Print the Average Miles Walked
    sum = 0
    for t in miles_walked:
        sum = sum + t
    avg = sum / len(miles_walked)
    Space()
    print("Average Miles Walked:", "{:0.2f}".format(avg))
    
    # End Main
    Space()
    print("End of The Program!")

# Call Main
Main()
        
# End Assignment