#====================================================================================
# Jake Watkins, Thursday 11:30am
# Watkin81@purdue.edu
# PROGRAM DESCRIPTION
#
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#====================================================================================

# Since I need line spaces in this program, this will save time
def Space():
    print("")

# Header Print for Lab Title
print("This is InLab02 for CNIT155 by Jake Watkins")
Space()

# Ask the User for a Float Input
# Find the Variable Type of the Input
# Display the Information
studentCount = int(input("Enter the Number of Students in CNIT 155: "))
studentVarType = type(studentCount)
print("The Number of Students in CNIT 155 is", studentCount)
print("The Data Type for the Number of Students is", studentVarType)
Space()

# Ask the User for a Float Input
# Find the Variable Type of the Input
# Display the Formatted Information
textbookPrice = float(input("Enter the Price of the Textbook: "))
priceVarType = type(textbookPrice)
print("The Price of the Textbook is $", '{0: .2f}'.format(textbookPrice))
print("The Data Type for the Number of Students is", priceVarType)
Space()

# Get Users Temprature Input in Float Form
# Subtract 32 and Multiply the Temprature by 5/9 to find the Temprature in Celcius
# Find the Variable Type of the Input
# Round and Print The Outputs
tempF = float(input("Enter Today's Temprature in Fahrenheit (F): "))
tempC = ((tempF - 32) * (5/9))
tempC = round(tempC, 2)
tempVarType = type(tempF)
print("Today's Temprature in Celcius is", tempC, "Degrees")
print("The Data Type for the Temprature is", tempVarType)