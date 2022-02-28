#====================================================================================
# Jake Watkins, Thursday 11:30am
# Watkin81@purdue.edu
# This Program uses Nested For Loops to Create Patterns with User Picked Values. This
# Includes a Table and many Variations of Triangles made of Stars and Numbers.
#
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#====================================================================================

# Import Math
import math

# Define Main Function
def Main():
    
    # Define the Header
    def Header():
        print("*******************************************")
        print("*          CNIT155 Assignment 06          *")
        print("*                                         *")
        print("*               Nested Loops              *")
        print("*******************************************")
        
    # Since I need line spaces in this program, this will save time
    def Space():
        print("")
        
    # Run the Header code so it displays at the top
    Header()
    
    # Create the Loop Variable
    loop = True
    
    # Run the Loop, this will keep running the menu after each calculation until the user exits the program (until loop = False)
    while loop == True:
        
        # Print a List of Operations for User to Select From
        Space()
        print("         Nested Loops Practice Menu       ")
        print("===========================================")
        print("1. Print A Multiplication Table")
        print("2. N for N times with commas")
        print("3. The Table of Stars")
        print("4. The Inverted Triangle")
        print("5. Exit Program")
        print("===========================================")
        Space()
        
        # Obtain the User's Selection so we know what to Calculate
        selection = str(input("Please Select One of the Operations: "))
    
        # --- MAIN IF SECTION ---
        # This is the Start of the Huge If Statement Chain
        
        # PART A - MULTIPLICATION TABLE
        if (selection == "1"):
            print("Option 1 Selected: Print A Multiplication Table")
            Space()
            # Get the User's Value of N
            nA = int(input("Enter a Number for N: "))
            Space()
            print("Displaying A", nA, "X", nA, "Multiplication Table")
            # For Loop to Cycle Numbers and Print them
            # To create the Table, I use X and Y values, and Multiply them together
            for nAX in range(1, nA+1):
                nAOutput = ""
                for nAY in range(1, nA+1):
                    nAOutput += str(nAX * nAY).zfill(2) + " "
                print(nAOutput)
                # Added zfill command to the string so all numbers in table are the same size

        # PART B - COMMA LIST
        elif (selection == "2"):
            print("Option 2 Selected: N for N Times with Commas")
            Space()
            # Get the User's Value of N
            nB = int(input("How many Lines should be Printed: "))
            # For Loop to Cycle Numbers
            for nB in range(nB+1):
                for nBY in range(nB):
                    # Create the Line
                    print(nB, end=",")
                # Start a New Line
                print("")
            
        # PART C - TABLE OF STARS
        elif (selection == "3"):
            print("Option 3 Selected: A Table of Stars")
            Space()
            # Get the User's Value of N
            nC = int(input("How many Rows of Stars should be Printed: "))
            print("Displaying", nC, "Row(s) of Stars")
            # For Loop to Cycle Numbers
            nCY = nC - 1
            for nC in range(0, nC):
                for nCX in range(0, nCY):
                    # Create the Spaces on the Same Line
                    print(end="  ")
                nCY = nCY - 1
                for nCX in range(0, nC+1):
                    # Print the Stars after Spaces
                    print("*", end=" ")
                    # Go to New Line
                print("")

        # PART D - INVERTED TRIANGLE
        elif (selection == "4"):
            print("Option 4 Selected: An Inverted Triangle")
            Space()
            # Get the User's Value of N
            nD = int(input("What Size of Triangle should be Printed: "))
            print("Displaying", nD, "Row(s) of The Triangle")
            # For Loop to Cycle Numbers
            for nDX in range(nD, 0, -1):
                for nDY in range(nD - nDX):
                    # Create the Spaces on the Same Line
                    print(" ", end="")
                for nDY in range(2 * nDX - 1):
                    # Print the Stars between Spaces
                    print("*", end="")
                    # Go to New Line
                print("")
            
        # PART E - EXIT PROGRAM
        elif (selection == "5"):      
            print("Option 5 Selected: Good Bye!")
            # Turn the Loop Off
            loop = False
            
        # PART G - ALL OTHER CASES
        else:
            # Print an Error Message for the User
            print("Invalid Input Entered!")
            print("Please Enter your choice between 1 and 5.")

# Call Main
Main()
        
# End Assignment