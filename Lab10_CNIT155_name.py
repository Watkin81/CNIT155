#====================================================================================
# Jake Watkins, Thursday 11:30am
# Watkin81@purdue.edu
# This Program takes a List of Scores from a file, calculates information, and writes
# the info to a file. The Try function is used to make sure the files open properly.
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
    print("*               CNIT155 Lab 10            *")
    print("*                                         *")
    print("*            Scores List and Files        *")
    print("*******************************************")
    Space()
    
# Since I need line spaces in this program, this will save time
def Space():
    print("")
    
    
# Define Main Function
def Main():
        
    # Run the Header code so it displays at the top
    Header()
    
    # Create the Variables and Lists
    scores = []
    
    # Try Function to Open Files
    try:
        inputFile = open("scores.txt", "r")
        outputFile = open("scores_stat.txt", "w")
        
        # Read the Scores Text File
        scores = inputFile.readlines()
        
        # List Compression to Change Strings to Floats
        scores = ([float(x) for x in scores])
        
        # Print Split Data
        print("Printing the Contents of the File...")
        Space()
        print(scores)      
        
        # Calculate: MAX MIN LEN AVG
        maxScore = max(scores)
        minScore = min(scores)
        length = len(scores)
        avg = ((sum(scores)) / (len(scores)))
        
        # Write Information to a New File
        outputFile.write("The Number of Scores in the List is " +str("{:0.2f}".format(length))+"\n")
        outputFile.write("The Average of Scores in the List is " +str("{:0.2f}".format(avg))+"\n")
        outputFile.write("The Maximum Score in the List is " +str("{:0.2f}".format(maxScore))+"\n")
        outputFile.write("The Minimum Score in the List is " +str("{:0.2f}".format(minScore))+"\n")
        
        # Close Files when Done
        inputFile.close()
        outputFile.close()
    
    # If the File cannot be found, give an error
    except FileNotFoundError:
        print("The Program Failed to Open the File. Please Check the Following:")
        print("    - The File to Read is Located in the Same Folder as This Program.")
        print("    - The File's Name is Spelled Correctly.")

    # End Main

# Call Main
Main()
        
# End Assignment