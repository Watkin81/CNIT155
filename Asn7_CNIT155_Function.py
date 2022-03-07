#====================================================================================
# Jake Watkins, Thursday 11:30am
# Watkin81@purdue.edu
# This Program Uses Functions and For Loops to Provide Outputs from Operations
# From User Inputted Values.
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
    print("*          CNIT155 Assignment 07          *")
    print("*                                         *")
    print("*          User Defined Functions         *")
    print("*******************************************")
    
# Since I need line spaces in this program, this will save time
def Space():
    print("")

# Define Factorial Function
def Factorial(nA, factorial):
    for nAX in range(1, nA + 1):
        # Multiply
        factorial = factorial * nAX
    return factorial
    
# Define Sum Odds Function
def SumOdds(nB, nB2, nBSum):
    for nB in range(nB, nB2 + 1):
        # If the Number has a Remainder, it is Odd
        if (nB % 2 == 1):
            print(nB)
            nBSum = nBSum + nB 
    return nBSum

# Define Sum Inverse Function
def SumInverse(nC, nC2, nCSum):
    for nC in range(nC, nC2 + 1):
        print("1 /", nC)
        # Create the Inverse, and Add
        nCSum = nCSum + (1 / nC)  
    return nCSum
    
# Define Find Character Function
def FindChar(nDstr, nDchar, nDcount):
    for character in nDstr:
        # Check if Character Matches
        if character == nDchar:
            nDcount = nDcount + 1
        else:
            # If it Doesn't Match, Skip that Character
            pass
    return nDcount


# Define Main Function
def Main():
        
    # Run the Header code so it displays at the top
    Header()
    
    # Create the Loop Variable
    loop = True
    
    # Run the Loop, this will keep running the menu after each calculation until the user exits the program (until loop = False)
    while loop == True:
        
        # Print a List of Operations for User to Select From
        Space()
        print("         User Defined Functions Menu       ")
        print("===========================================")
        print("1. Compute N Factorial")
        print("2. Sum of All Odd Numbers from N1 to N2 (N1 <= N2)")
        print("3. Sum of the Inverse of Numbers Between N1 and N2 (N1 <= N2)")
        print("4. Find Number of Characters")
        print("5. Exit Program")
        print("===========================================")
        Space()
        
        # Obtain the User's Selection so we know what to Calculate
        selection = str(input("Please Select One of the Operations: "))
    
        # --- MAIN IF SECTION ---
        # This is the Start of the Huge If Statement Chain
        
        # PART A - N FACTORIAL
        if (selection == "1"):
            print("Option 1 Selected: Compute N Factorial")
            Space()
            # Inputs and Setting Vars
            factorial = 1
            nA = int(input("Please Enter a Value for N: "))
            # Run and Print Formatted Return Value
            print(nA, "! is equal to", Factorial(nA, factorial))

        # PART B - SUM ODD
        elif (selection == "2"):
            print("Option 2 Selected: Sum of All Odd Numbers from N1 to N2 (N1 <= N2)")
            Space()
            # Inputs and Setting Vars
            nBSum = 0
            nB = int(input("Please Enter a Value for N1: "))
            nB2 = int(input("Please Enter a Value for N2: "))
            # Run and Print Formatted Return Value
            print("The Sum of the Odd Numbers is: ", SumOdds(nB, nB2, nBSum))            
            
        # PART C - SUM INVERSE
        elif (selection == "3"):
            print("Option 3 Selected: Sum of the Inverse of Numbers Between N1 and N2 (N1 <= N2)")
            Space()
            # Inputs and Setting Vars
            nCSum = 0
            nC = int(input("Please Enter a Value for N1: "))
            nC2 = int(input("Please Enter a Value for N2: "))
            # Run and Print Formatted Return Value
            print("The Sum of the Inverse Numbers is: ", format(SumInverse(nC, nC2, nCSum), '.2f'))

        # PART D - NUMBER OF CHARACTERS
        elif (selection == "4"):
            print("Option 4 Selected: Find Number of Characters")
            Space()
            # Inputs and Setting Vars
            nDcount = 0
            nDstr = str(input("Please Enter a String: "))
            nDchar = str(input("Please Enter a Character to Count: "))
            # Run and Print Formatted Return Value
            print("The Character", nDchar, "Appeared", FindChar(nDstr, nDchar, nDcount), "Times.")
            
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