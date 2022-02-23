#====================================================================================
# Jake Watkins, Thursday 11:30am
# Watkin81@purdue.edu
# This Program has the User pick between different calculations, all of which take 
# a N Value and use While Loops to solve.
#
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#====================================================================================

# Define Main Function
def Main():
    
    # Import Math
    import math
    
    # Define the Header
    def Header():
        print("*******************************************")
        print("*          CNIT155 Assignment 05          *")
        print("*                                         *")
        print("*           While Loops Practice          *")
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
        print("         While Loops Practice Menu         ")
        print("===========================================")
        print("A. Sum of Odd Natural Numbers from 1 to N")
        print("B. Sum of Squares of Odd Natural Numbers from 1 to N")
        print("C. Sum of Cubes of Even Natural Numbers from 1 to N")
        print("D. Factorial of N")
        print("E. Multiplication Table of N")
        print("F. Exit Program")
        print("===========================================")
        Space()
        
        # Obtain the User's Selecion so we know what to Calculate
        selection = str(input("Please Select One of the Opeartions: "))
    
        # --- MAIN IF SECTION ---
        # This is the Start of the Huge If Statement Chain
        
        # PART A - ODD SUM
        if (selection == "A" or selection == "a"):
            print("Option A Selected: Sum of Odd Natural Numbers from 1 to N.")
            Space()
            # Get the User's Value of N
            nA = int(input("Enter a Natural Number for N: "))
            Space()
            # While Loop to Find Odd Numbers an Add Them Together
            print("Displaying Odd Natural Numbers from 1 to", nA)
            nAsum = 0
            nAcount = nA
            # Loop Until all Numbers Checked
            while nAcount > 0:
                # if it devides with a remainder, it is odd
                if nAcount % 2 != 0:
                    # Print and add to sum if odd
                    print(nAcount)
                    nAsum = nAsum + nAcount
                nAcount = nAcount - 1
            Space()
            # Print the Sum
            print("The Sum of the Odd Natural Numbers from 1 to", nA, "is", nAsum)
            
        # PART B - ODD SQUARES
        elif (selection == "B" or selection == "b"):
            print("Option B Selected: Sum of Squares of Odd Natural Numbers from 1 to N.")
            Space()
            # Get the User's Value of N
            nB = int(input("Enter a Natural Number for N: "))
            Space()
            # While Loop to Find Odd Numbers an Add Them Together
            print("Displaying Odd Natural Numbers Squares from 1 to", nB)
            nBsum = 0
            nBcount = nB
            # Loop Until all Numbers Checked
            while nBcount > 0:
                # if it devides with a remainder, it is odd
                if nBcount % 2 != 0:
                    # Calculate the Square, Print, and add to sum
                    nBsquare = nBcount ** 2
                    print(nBsquare)
                    nBsum = nBsum + nBsquare
                nBcount = nBcount - 1
            Space()
            # Print the Sum
            print("The Sum of the Odd Natural Numbers Squares from 1 to", nB, "is", nBsum)     
            
        # PART C - EVEN CUBES
        elif (selection == "C" or selection == "c"):
            print("Option C Selected: Sum of Cubes of Even Natural Numbers from 1 to N.")
            Space()
            # Get the User's Value of N
            nC = int(input("Enter a Natural Number for N: "))
            Space()
            # While Loop to Find Odd Numbers an Add Them Together
            print("Displaying Even Natural Numbers Cubes from 1 to", nC)
            nCsum = 0
            nCcount = nC
            # Loop Until all Numbers Checked
            while nCcount > 0:
                # if it devides without a remainder, it is even
                if nCcount % 2 == 0:
                    # Calculate the Square, Print, and add to sum
                    nCcube = nCcount ** 3
                    print(nCcube)
                    nCsum = nCsum + nCcube
                nCcount = nCcount - 1
            Space()
            # Print the Sum
            print("The Sum of the Even Natural Numbers Cubes from 1 to", nC, "is", nCsum)    
            
        # PART D - FACTORIAL
        elif (selection == "D" or selection == "d"):
            print("Option D Selected: Find the Factorial of N.")
            Space()
            nD = int(input("Enter a Natural Number for N: "))
            # While Loop to Cycle through all numbers and multiply them
            nDsum = 1
            nDcount = nD        
            # Loop Until all Numbers Checked
            while nDcount > 0:
                nDsum = nDsum * nDcount
                nDcount = nDcount - 1
            Space()
            # Print the Sum
            print("The Factorial of", nD, "is", nDsum)
            
        # PART E - MULTIPLICATION TABLE
        elif (selection == "E" or selection == "e"):
            print("Option E Selected: Multiplication Table of N.")
            Space()
            # Get the User's Value of N
            nE = int(input("Enter a Natural Number for N: "))
            Space()
            # While Loop to List Through Multiplication Tables
            nEcount = 1
            nEsum = 0
            print("Displaying Multiplicaion Table of", nE)
            # Loop For 10 Numbers
            while nEcount <= 10:
                nEsum = nE * nEcount
                print(nE, "x", nEcount, "=", nEsum) 
                nEsum = 0
                nEcount = nEcount + 1
            
        # PART F - EXIT PROGRAM
        elif (selection == "F" or selection == "f"):      
            print("Option F Selected: Good Bye!")
            # Turn the Loop Off
            loop = False
            
        # PART G - ALL OTHER CASES
        else:
            # Print an Error Message for the User
            print("Invalid Input Entered!")
            print("Please Enter your choice between A and F.")

# Call Main
Main()
        
# End Assignment