#====================================================================================
# Jake Watkins, Thursday 11:30am
# Watkin81@purdue.edu
# This Lab Takes User's Price Inputs in Usd and converts them to Euros, as well as
# FInding averages and displaying them. Uses Lists and Functions.
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
    print("*                CNIT155 Lab 9            *")
    print("*                                         *")
    print("*                 Conversion              *")
    print("*******************************************")
    Space()
    
# Since I need line spaces in this program, this will save time
def Space():
    print("")

# Covert USD Values to Euro by Multiplying by 0.85
def UsdToEuro(lst):
    euro = [i * 0.85 for i in lst]
    return euro

# Function to Display USD and Euro Infomation
def PrintInfo(lst, lst2):
    y = 0
    print("\tUSD ($)\t\tEuro (E)")
    print("========================================")
    for x in lst:
        print("\t", "{:0.2f}".format(lst[y]), "\t\t", "{:0.2f}".format(lst2[y]))
        y = y + 1

# Find the Average of List Values
def Avg(lst):
    sum = 0
    for t in lst:
        sum = sum + t
    avg = sum / len(lst)
    return avg

# Find all Prices Below 50
def FindPrice(lst):
    temp = []
    for s in lst:
        if (s < 50):
            temp.append(s)
    return temp


# Define Main Function
def Main():
        
    # Run the Header code so it displays at the top
    Header()
    
    # Create the Variables and Lists
    usd = []
    euro = []
    
    # Get List Inputs from User on Loop
    while True:
        userInput = float(input("Enter a Price in USD. Use -1 to Stop Data Entry: "))
        if (userInput == -1):
            break
        else:
            usd.append(userInput)
            continue
    
    # Print Length of List to Display Number of Entries
    Space()
    print("Number of Prices Entered:", len(usd))
    Space()
    
    # Convert the Values to Euro
    euro = UsdToEuro(usd)
    
    # Display the Information
    PrintInfo(usd, euro)    
    
    # Find the Averages of Both Currencies
    avg1 = Avg(usd)
    avg2 = Avg(euro)
    
    # Find the Prices Below 50 Dollars
    usdsublist = FindPrice(usd)
    eurosublist = UsdToEuro(usdsublist)
    
    # Print all the Information
    Space()
    print("========================================")
    print("=============== AVERAGES ===============")
    Space()
    print ("The Average of Prices in USD is $", "{:0.2f}".format(avg1))
    print ("The Average of Prices in EURO is E", "{:0.2f}".format(avg2))
    Space()
    print("====== Price(s) under $50 is(are) ======")
    print("\tUSD\t\tEURO")
    print("       -------         ------- ")
    
    w = 0
    for z in usdsublist:
        print("\t", "{:0.2f}".format(usdsublist[w]), "\t\t", "{:0.2f}".format(eurosublist[w]))
        w = w + 1    
    
    Space()
    print("========================================")
    
    # End Main

# Call Main
Main()
        
# End Assignment