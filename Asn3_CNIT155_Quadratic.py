#====================================================================================
# Jake Watkins, Thursday 11:30am
# Watkin81@purdue.edu
# This Program Takes User Inputs in the form of Coefficients, and solves for the roots
# of the Quadratic Equation. This is done through Multiple Equations and Cascading IF Statements.
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
        print("*          CNIT155 Assignment 03          *")
        print("*                                         *")
        print("*             Quadratic Roots             *")
        print("*******************************************")
        
    # Sinmpler way to add line spacings
    def Space():
        print("")
        
    # Run the Header code so it displays at the top
    Header()
    Space()
    
    # Get Users Coefficient Inputs and Define Variables
    smallCoef = 0
    CoA = float(input("Enter Coefficient A: "))
    CoB = float(input("Enter Coefficient B: "))
    CoC = float(input("Enter Coefficient C: "))
    Space()
    
    # Print the Quadratic Formula with Above Variables
    print ("Your Quadratic Equation:", CoA, "*X^2 +", CoB, "*X +", CoC, "= 0")
    Space()
    
    # Solve for the Discriminant and Print it
    discrim = (CoB ** 2) - (4 * CoA * CoC)
    print("The Discriminant is:", format(discrim, '.2f'))   
    Space()
    
    # Find the Number of Roots based on the Value of the Discriminant
    # Then, Find the Value of the Roots with a Variation of the Quadratic Forumla
    if (discrim < 0):
        print("The Equation has No Real Roots.")
    elif (discrim == 0):
        oneRoot = -CoB / (2 * CoA)
        print ("The Equation has Only One Root:", format(oneRoot, '.2f'))
    elif (discrim > 0):
        twoRoot1 = (-CoB + math.sqrt(discrim)) / (2 * CoA)
        twoRoot2 = (-CoB - math.sqrt(discrim)) / (2 * CoA)
        print ("The Equation has Two Real Roots:", format(twoRoot1, '.2f'), "and", format(twoRoot2, '.2f'))
    Space()
    
    # Find and Print the Smallest Coefficient by Comparing the Values
    if (CoA < CoB and CoA < CoC):
        smallCoef = CoA
    elif (CoB < CoA and CoB < CoC):
        smallCoef = CoB
    else:
        smallCoef = CoC
    print("The Smallest Coefficient is:", format(smallCoef, '.2f'))
    
# Call Main
Main()
    
# End Assignment