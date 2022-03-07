#====================================================================================
# Jake Watkins, Thursday 11:30am
# Watkin81@purdue.edu
# This Program dddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
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
    print("*               Jake Watkins              *")
    print("*            Watkin81@purdue.edu          *")
    print("*            CNIT 155 - InLab 06          *")
    print("*******************************************")

# Define Validate Function
# Checks if the sum of two sides is greater than the other side
def validate(a,b,c):
    if ((a + b) > c):
        if ((a + c) > b):
            if ((b + c) > a):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
# Define Area Finding Function
def computeArea(a,b,c):
    s = 0.0
    area = 0.0
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Define Find Minimum Side Value
def findMin(a,b,c):
    if ((a < b) and (a < c)):
        return a
    elif ((b < a) and (b < c)):
        return b
    elif ((c < b) and (c < a)):
        return c
    else:
        # if neither of the three values are less than the other, than the value doesn't matter since they are all equal
        return a
    
# Define Find Maximum Size Value
def findMax(a,b,c):
    if ((a > b) and (a > c)):
        return a
    elif ((b > a) and (b > c)):
        return b
    elif ((c > b) and (c > a)):
        return c
    else:
        # if neither of the three values are greater than the other, than the value doesn't matter since they are all equal
        return a

# Since I need line spaces in this program, this will save time
def Space():
    print("")

# Define Main Function
def Main():
        
    # Run the Header code so it displays at the top
    Header()
    
    # Create the Loop Variable
    loop = True
    
    # Run the Loop, this will keep running the menu after each calculation until the user exits the program (until loop = False)
    while loop == True:
        
        Space()
        # Obtain the User's Selection so we know what to Calculate
        a = float(input("Enter the Length of the Triangle's A Side: "))
        b = float(input("Enter the Length of the Triangle's B Side: "))
        c = float(input("Enter the Length of the Triangle's C Side: "))
        
        # Visual only Validating Text
        Space()
        print("Validating Triangle...")
        Space()
    
        # Runs the Validate Function to Check if the Users Inputted Values make a Valid Triangle
        if validate(a,b,c) == True:
            print("This is a Valid Triangle!")
            # if Valid, Compute the Area
            areaVal = computeArea(a,b,c)
            print("The Area of the Triangle is", format(areaVal, '.2f'))
            # Find the Min and Max Sides and Print
            min = findMin(a,b,c)
            max = findMax(a,b,c)
            print("The Shortest Side is", min,"and the Longest Side is", max)
            
        # If the Triangle is Not Valid, Continue
        else:
            print("This is Not a Valid Triangle!")
            continue
            
        while True:
            Space()
            # Ask if the User would like to Compute again
            flag=str(input("Do you want to compute again? (Y/N): "))
            if (flag == "y" or flag == "Y"):
                break
            elif (flag == "n" or flag == "N"):
                Space()
                print("- Program Terminated -")
                loop = False
                return False
            else:
                print("Invalid Input Entered!")
                print("Please Enter your choice of Y or N.")
            
# Call Main
Main()
        
# End Assignment