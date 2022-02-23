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
        print("*              CNIT155 Lab 04             *")
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
        print("1. Print all Natural Numbers from 1 to N")
        print("2. Add Up all Natural Numbers from 1 to N")
        print("3. Add Up all Even Natural Numbers from 1 to N")
        print("4. Compute the Sum of the Square Numbers Between 1 and N")
        print("5. Compute the Sum and Average of the Cube Numbers Between 1 and N")
        print("6. Exit Program")
        print("===========================================")
        Space()
        
        # Obtain the User's Selecion so we know what to Calculate
        selection = str(input("Please Select One of the Opeartions: "))
    
        # --- MAIN IF SECTION ---
        # This is the Start of the Huge If Statement Chain
        
        # PART A - PRINT NATURAL
        if (selection == "1"):
            print("Option A Selected: Print all Natural Numbers from 1 to N")
            Space()
            # Get the User's Value of N
            nA = int(input("Enter a Natural Number for N: "))
            Space()
            # While Loop to Cycle Numbers and Print them
            print("Displaying Natural Numbers from 1 to", nA)
            nAcount = nA
            # Loop Until all Numbers Checked
            while nAcount > 0:
                print(nAcount)
                nAcount = nAcount - 1
            
        # PART B - SUM NATURAL
        elif (selection == "2"):
            print("Option 2 Selected: Add Up all Natural Numbers from 1 to N.")
            Space()
            # Get the User's Value of N
            nB = int(input("Enter a Natural Number for N: "))
            Space()
            # While Loop to Cycle Numbers and Add Them Together
            print("Displaying Natural Numbers and Adding them from 1 to", nB)
            nBsum = 0
            nBcount = nB
            # Loop Until all Numbers Checked
            while nBcount > 0:
                # Calculate the Square, Print, and add to sum
                print(nBcount)
                nBsum = nBsum + nBcount
                nBcount = nBcount - 1
            Space()
            # Print the Sum
            print("The Sum of the Natural Numbers from 1 to", nB, "is", nBsum)  
            
        # PART C - SUM EVEN
        elif (selection == "3"):
            print("Option 3 Selected: Add Up all Even Natural Numbers from 1 to N")
            Space()
            # Get the User's Value of N
            nC = int(input("Enter a Natural Number for N: "))
            Space()
            # While Loop to Find Even Numbers an Add Them Together
            print("Displaying Even Natural Numbers from 1 to", nC)
            nCsum = 0
            nCcount = nC
            # Loop Until all Numbers Checked
            while nCcount > 0:
                # if it devides without a remainder, it is even
                if nCcount % 2 == 0:
                    # Print, and add to Sum
                    print(nCcount)
                    nCsum = nCsum + nCcount
                nCcount = nCcount - 1
            Space()
            # Print the Sum
            print("The Sum of the Even Natural Numbers from 1 to", nC, "is", nCsum)    
            
        # PART D - SUM SQUARES
        elif (selection == "4"):
            print("Option 4 Selected: Compute the Sum of the Square Numbers Between 1 and N.")
            Space()
            nD = int(input("Enter a Natural Number for N: "))
            Space()
            # While Loop to Cycle through all numbers and squares / add them
            print("Displaying the Squares of Numbers from 1 to", nD)
            nDsum = 0
            nDcount = nD        
            # Loop Until all Numbers Checked
            while nDcount > 0:
                nDsquare = nDcount ** 2
                print(nDsquare)
                nDsum = nDsum + nDsquare
                nDcount = nDcount - 1
            Space()
            # Print the Sum
            print("The Sum of the Squares from 1 to", nD, "is", nDsum)
            
        # PART E - SUM AND AVERAGE OF CUBES
        elif (selection == "5"):
            print("Option 5 Selected: Compute the Sum and Average of the Cube Numbers Between 1 and N.")
            Space()
            # Get the User's Value of N
            nE = int(input("Enter a Natural Number for N: "))
            Space()
            # While Loop to Sum and Average the Squares of the Numbers
            print("Displaying the Cubes of Numbers from 1 to", nE)
            nEcount = nE
            nEsum = 0
            # Loop Until all Numbers Checked
            while nEcount > 0:
                nEcubed = nEcount ** 3
                print(nEcubed)
                nEsum = nEsum + nEcubed
                nEcount = nEcount - 1
            # Get the Average of the Cubes
            nEaverage = nEsum / nE
            Space()
            # Print the Sum
            print("The Sum of the Cubes from 1 to", nE, "is", nEsum)
            # Print the Average
            print("The Average of the Cubes from 1 to", nE, "is", format(nEaverage, '.2f'))            
            
        # PART F - EXIT PROGRAM
        elif (selection == "6"):      
            print("Option 6 Selected: Good Bye!")
            # Turn the Loop Off
            loop = False
            
        # PART G - ALL OTHER CASES
        else:
            # Print an Error Message for the User
            print("Invalid Input Entered!")
            print("Please Enter your choice between 1 and 6.")

# Call Main
Main()
        
# End Assignment