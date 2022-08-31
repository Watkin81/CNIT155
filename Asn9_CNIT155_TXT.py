#====================================================================================
# Jake Watkins, Thursday 11:30am
# Watkin81@purdue.edu
# This Program takes inputs from a file, and seperated the information so the program
# can read it. After, calculations are written to the file to give helpful information.
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
    print("*          CNIT155 Assignment 09          *")
    print("*                                         *")
    print("*                   Files                 *")
    print("*******************************************")
    
# Since I need line spaces in this program, this will save time
def Space():
    print("")


# Define Main Function
def Main():
        
    # Run the Header code so it displays at the top
    Header()
    Space()
    
    # Create the List Variables
    names = []
    scores = []
    temp = []
    
    # start of try
    try:
        # Open Files
        file = open("input.txt", "r")
        output = open("output.txt", "w")
        for line in file:
            # Split and Store the Data
            temp = line.strip().split(",")
            names.append(temp[0])
            scores.append(temp[1])
            
        # Print Split Data
        print("Printing the Contents of the File...")
        print(names)
        print(scores)
        
        # Find MAX and MIN
        max = scores[0]
        for i in scores:
            if i > max:
                max = i
        min = scores[0]
        for j in scores:
            if j < min:
                min = j
        print(max, min)
        
        maxNames = []
        for k in scores:
            maxPos = scores.index(max)
        tempName = names[maxPos]
        maxNames.append(tempName)
        print(maxNames)        
        
        minNames = []
        for l in scores:
            minPos = scores.index(min)
        tempName = names[minPos]
        minNames.append(tempName)
        print(minNames)
        
        output.write("Maximum Score is: " + max)
        output.write("Minimum Score is: " + min)
        
        # Print to Inform User about Updates 
        Space()
        print("Scores Have Been Updated! Check the Output File!")
        
        # Close the Files
        file.close()
        output.close()
        
    # If the File cannot be found, give an error
    except FileNotFoundError:
        print("The Program Failed to Open the File. Please Check the Following:")
        print("    - The File to Read is Located in the Same Folder as This Program.")
        print("    - The File's Name is Spelled Correctly.")

    # End Main

# Call Main
Main()
        
# End Assignment