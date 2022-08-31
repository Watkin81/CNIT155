#====================================================================================
# Jake Watkins, Thursday 11:30am
# Watkin81@purdue.edu
# This Program takes a List of Books from a file, calculates information, and writes
# the info to a file. x
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
    print("*               CNIT155 Lab 11            *")
    print("*                                         *")
    print("*             Books List and Files        *")
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
    books = []
    longBooks = []
    fixedBooks = []
    
    # Try Function to Open Files
    try:
        inputFile = open("books.txt", "r")
        outputFile = open("books_analysis.txt", "w")
        
        # Read the Scores Text File
        books = inputFile.readlines()
        
        # Print Book Data
        print("Printing the Contents of the File...")
        Space()
        print(books)      
        
        # 1) Calculate: Book Count
        booksCount = len(books)
        # Write Book Count
        outputFile.write("1) The Number of Books in the File : " + str(booksCount) + "\n" + "\n")
                
        # 2) Calculate: More han Two Words in Title
        for line in books:
            titleWords = line.split(" ")
            if (len(titleWords) > 2):
                longBooks.append(line)
        # Write The List of Books with More than 2 Words
        outputFile.write("2) Titles of Books with More than Two Words:" + "\n")
        for y in longBooks:
            outputFile.write(y)
        outputFile.write("\n" + "\n")
        
        # 3) Using the Title Function in a for loop to Fix Titles, and Writing the Information
        outputFile.write("3) Organized Book Titles:" + "\n")
        for line in books:
            temp = line.title()
            outputFile.write(str(temp))
        
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