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
        print("*              CNIT155 Lab 05             *")
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
        print("               For Loops Lab               ")
        print("===========================================")
        print("1. Display & Add Natural Numbers from N to 1")
        print("2. Multiplication Table of N")
        print("3. The Pyramid of Stars")
        print("4. The Pyramid of Numbers")
        print("5. Exit Program")
        print("===========================================")
        Space()
        
        # Obtain the User's Selection so we know what to Calculate
        selection = str(input("Please Select One of the Operations: "))
    
        # --- MAIN IF SECTION ---
        # This is the Start of the Huge If Statement Chain
        
        # PART A - N TO 1 DISPLAY
        if (selection == "1"):
            print("Option 1 Selected: Display and Add Natural Numbers from N to 1")
            Space()
            # Get the User's Value of N
            nA = int(input("Enter a Number for N: "))
            Space()
            nASum = 0
            print("Displaying Natural Numbers from", nA, "to 1")
            # Loop from Highest Value (N) to 1, with a -1 Step
            for nA in range(nA, 0 , -1):
                print(nA)
                # Add the Value to the Sum
                nASum = nASum + nA
                nA = nA - 1
            # Print the Sum after Looping
            print("Sum:", nASum)
            
        # PART B - MULTIPLICATION TABLE
        elif (selection == "2"):
            print("Option 2 Selected: Multiplicaton Table")
            Space()
            # Get the User's Value of N
            nB = int(input("Enter a Natural Number for N: "))
            # While Loop to List Through Multiplication Tables
            print("Displaying The Multiplicaion Table of", nB)
            # Loop For 10 Numbers
            for nBX in range(1, 11):
                # Print the Line
                print(nB, "x", nBX, "=", nB * nBX)
            
        # PART C - PYRAMID OF STARS
        elif (selection == "3"):
            print("Option 3 Selected: A Pyramid of Stars")
            Space()
            # Get the User's Value of N
            nC = int(input("How many Rows of Stars should be Printed: "))
            print("Displaying", nC, "Row(s) of Stars")
            # For Loop to Cycle Numbers
            for nC in range(0, nC):
                # For Loop for Number of Stars
                for nCX in range(0, nC+1):
                    # Print
                    print("* ", end="")
                # New Line after Each Star
                print("")

        # PART D - PYRAMID OF NUMBERS
        elif (selection == "4"):
            print("Option 4 Selected: An Inverted Triangle")
            Space()
            # Get the User's Value of N
            nD = int(input("How many Rows of Numbers should be Printed: "))
            # For Loop to Cycle Numbers
            for nDX in range(nD, 0, -1):
                for nDY in range(1, nDX+1):
                    # Create the Line
                    print(nDY, end=" ")
                # Start a New Line
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