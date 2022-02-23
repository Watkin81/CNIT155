#====================================================================================
# Jake Watkins, Thursday 11:30am
# Watkin81@purdue.edu
# This Program gets float inputs from the user and then calculates the side area, 
# bottom area, and volume of a pool. This program uses the math function for calculations.
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
        print("*             CNIT155  Lab 03             *")
        print("*                                         *")
        print("*            Pool  Calculators            *")
        print("*******************************************")
        
    # Since I need line spaces in this program, this will save time
    def Space():
        print("")
        
    # Run the Header code so it displays at the top
    Header()
    Space()
    
    # Gather the Users Input for the different Depths of the Pool
    poolD1 = float(input("Enter a Value for Depth1 (D1): "))
    poolD2 = float(input("Enter a Value for Depth2 (D2): "))
    
    # Check to make sure the Second Depth is Greater than the First Depth
    if (poolD2 > poolD1):
        # D1 is smaller, continue wih program
        poolWidth = float(input("Enter a Value for Width (W): "))
        poolLength = float(input("Enter a Value for Length (L): "))
        
        # Cosmetic Calculating Text
        Space()
        print("Calculaing...")
        Space()
        
        # Doing the Math for the Side Area
        poolSideArea = (poolD1 + poolD2) * (poolLength / 2)
        
        # Doing the Math for the Bottom Area
        poolD3 = poolD2 - poolD1
        poolBottomArea = (math.sqrt((poolD3 ** 2) + (poolLength ** 2))) * poolWidth
        
        # Doing the Math for the Volume
        poolVolume = poolSideArea * poolWidth
        
        # Print the Outputs for our User to View
        print("The Side Area of the Pool is:", format(poolSideArea, '.2f'))  
        print("The Bottom Area of the Pool is:", format(poolBottomArea, '.2f'))  
        print("The Volume of the Pool is:", format(poolVolume, '.2f'))
        
    else:
        # D1 is larger, print error
        print("Invalid Input! D2 must be greater than D1!!!")     

# Call Main
Main()
            
# End Lab