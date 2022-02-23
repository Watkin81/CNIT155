#====================================================================================
# Jake Watkins, Thursday 11:30am
# Watkin81@purdue.edu
# This Program Allows the User to Pick from a List of Opertaions, and the Program 
# will Carry out the Operation. Operations Include Areas and Volumes of Shapes.
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
        print("*          CNIT155 Assignment 04          *")
        print("*                                         *")
        print("*       Area And Volume Calculators       *")
        print("*******************************************")
        
    # Since I need line spaces in this program, this will save time
    def Space():
        print("")
        
    # Run the Header code so it displays at the top
    Header()
    Space()
    
    # Print a List of Operations for User to Select From
    print("===========================================")
    print("A. Area Of A Rectangle")
    print("B. Area Of A Trapezoid")
    print("C. Volume Of A Sphere")
    print("D. Volume Of A Hexagonal Pyramid")
    print("E. Volume Of An Octagonal Prism")
    print("===========================================")
    Space()
    
    # Obtain the User's Selecion so we know what to Calculate
    selection = str(input("Please Select One of the Opeartions: "))
    Space()

    # --- MAIN IF SECTION ---
    # This is the Start of the Huge If Statement Chain
    
    # PART A - AREA RECTANGLE
    if (selection == "A" or selection == "a"):
        print("Option A Selected: Area of a Rectangle.")
        Space()
        # Get Rectangle Dimensions from the User for Calculation
        recWidth = float(input("Enter the Width of the Rectangle: "))
        recLength = float(input("Enter the Height of the Rectangle: "))
        Space()
        # Calculate the Area (Length * Width) and Print
        recArea = recLength * recWidth
        print("The Area of the Rectangle is", format(recArea, '.2f'))
        
    # PART B - AREA TRAPEZOID
    elif (selection == "B" or selection == "b"):
        print("Option B Selected: Area of a Trapezoid.")
        Space()
        # Get Trapezoid Dimensions from the User for Calculation
        trapShort = float(input("Enter the Short Base of the Trapezoid: "))
        trapLong = float(input("Enter the Long Base of the Trapezoid: "))
        trapHeight = float(input("Enter the Height of the Trapezoid: "))
        Space()
        # Calculate the Area (((A + B) / 2) * H) and Print
        trapArea = ((trapShort + trapLong) / 2) * trapHeight
        print("The Area of the Trapezoid is", format(trapArea, '.2f'))        
        
    # PART C - VOLUME SPHERE
    elif (selection == "C" or selection == "c"):
        print("Option C Selected: Volume of a Sphere.")
        Space()
        # Get Sphere Dimensions from the User for Calculation
        sphereRad = float(input("Enter the Radius of the Sphere: "))
        Space()
        # Calculate the Volume (((4/3) * pi) * R^3) and Print
        sphereVolume = ((4/3) * math.pi) * (sphereRad ** 3)
        print("The Volume of the Sphere is", format(sphereVolume, '.2f'))
        
    # PART D - VOLUME HEX PYRAMID
    elif (selection == "D" or selection == "d"):
        print("Option D Selected: Volume of a Hexagonal Pyramid.")
        Space()
        # Get Hex Pyramid Dimensions from the User for Calculation
        hexEdge = float(input("Enter the Base Edge of the Hexagonal Pyramid: "))
        hexHeight = float(input("Enter the Base Edge of the Hexagonal Pyramid: "))
        Space()
        # Calculate the Volume ((sqrt(3)/2) * (A ** 2)) * H) and Print
        hexVolume = ((math.sqrt(3)/2) * (hexEdge ** 2)) * hexHeight
        print("The Volume of the Hexagonal Pyramid is", format(hexVolume, '.2f'))    
        
    # PART E - VOLUME OCT PRISM
    elif (selection == "E" or selection == "e"):
        print("Option E Selected: Volume of an Octagonal Prism.")
        Space()
        # Get Oct Prism Dimensions from the User for Calculation
        octEdge = float(input("Enter the Base Edge of the Octagonal Prism: "))
        octHeight = float(input("Enter the Base Edge of the Octagonal Prism: "))
        Space()
        # Calculate the Volume ((2 * (1 + sqrt(2)) * (A ** 2)) * H) and Print
        octVolume = (2 * (1 + math.sqrt(2)) * (octEdge ** 2)) * octHeight
        print("The Volume of the Hexagonal Pyramid is", format(octVolume, '.2f'))           
        
    # PART F - ALL OTHER CASES
    else:
        # Print Error Message for User
        print("Invalid Input Entered!")
        print("Please Enter your choice between A and E.")

# Call Main
Main()
        
# End Assignment