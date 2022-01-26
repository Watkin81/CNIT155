#====================================================================================
# Jake Watkins, Thursday 11:30am
# Watkin81@purdue.edu
# This Program takes User Inputs and Converts them into different Units.
#
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#====================================================================================

# Define the Header
def Header():
    print("*******************************************")
    print("*          CNIT155 Assignment 02          *")
    print("*                                         *")
    print("*          Conversion Calculator          *")
    print("*******************************************")
    
# Since I need line spaces in this program, this will save time
def Space():
    print("")
    
# Run the Header code so it displays at the top
Header()
Space()

# Get the users name, and then display it
# This string is stored with the variable "name"
name = input("Enter your Name: ")
print("The Name Entered is", name)
Space()

# Get Users Weight Input in Float Form
# Devide the Pounds by 2.2046 to find Kilograms
# Round the Output
# Print Both Values for the User to Read
print("--- 1st. Pounds to Kilograms Converter ---")
weightInput = float(input("Enter the Weight in Pounds to Convert into Kilograms: "))
weightOutput = weightInput / 2.2046
weightOutput = round(weightOutput, 2)
print ("The Entered Weight in Pounds was", weightInput, "lb. This is", weightOutput, "kg!")
Space()

# Get Users Temprature Input in Float Form
# Multiply the Temprature by 9/5 and add 32 to find Fahrenheit
# Round and Print Both
print("--- 2nd. Celcius to Fahrenheit Converter ---")
tempratureInput = float(input("Enter the Temprature in Ceclius to Convert into Fahrenheit: "))
tempratureOutput = (tempratureInput * (9/5)) + 32
tempratureOutput = round(tempratureOutput, 2)
print ("The Entered Temprature was", tempratureInput, "C. This is", tempratureOutput, "F!")
Space()

# Get Users Distance Input in Float Form
# Multiply the Temprature by 9/5 and add 32 to find Fahrenheit
# Round and Print Both
print("--- 3rd. Miles to Kilometers Converter ---")
distanceInput = float(input("Enter a Distance in Miles to Convert into Kilometers: "))
distanceOutput = distanceInput * 1.609344
distanceOutput = round(distanceOutput, 2)
print ("The Entered Distance in Miles was", distanceInput, "mi. This is", distanceOutput, "km!")
Space()

# Get Users Height Input of Feet and Inches in Float Form
# Multiply the Feet by 12 for inches, and then convert the Inches into Cenitmeters by Multiplying by 2.54
# Round and Print All 3 Values
print("--- 4th. Feet and Inches to Centimeters Converter ---")
print("What is your Height in Feet and Inches?")
heightInputFeet = float(input("Feet?: "))
heightInputInches = float(input("Inches?: "))
heightOutputFeet = heightInputFeet * 12
heightOutput = heightOutputFeet + heightInputInches
heightOutput = heightOutput * 2.54
heightOutput = round(heightOutput, 2)
print ("Your Entered Height was", heightInputFeet, "Feet and", heightInputInches, "Inches. This is", heightOutput, "cm Tall!")
Space()

# End Assignment
print(">>>Thank you for using the Python Conversion Calculator!<<<")