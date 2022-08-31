#====================================================================================
# Jake Watkins, Thursday 11:30am
# Watkin81@purdue.edu
# This Assignment Uses Functions and Lists to convert information about certian products
# prices into tables with discounts, and certian Since
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
    print("*          CNIT155 Assignment 08          *")
    print("*                                         *")
    print("*                   Lists                 *")
    print("*******************************************")
    
# Since I need line spaces in this program, this will save time
def Space():
    print("")
    
# Print the Information
def PrintInfo(lst, lst2, lst3):
    infoNum = 0
    print("     NAME     .     ID     .     PRICE     ")
    print("===========================================")
    while infoNum < len(lst):
        print("    ", lst[infoNum], "        ", lst2[infoNum], "        ", format(lst3[infoNum], '.2f'))
        infoNum = infoNum + 1

# Multiply All List Values by 0.7
def Discount(lst):
    disPrices = [i * 0.7 for i in lst]
    return disPrices

# Find Averae of a List
def Average(lst):
    return sum(lst) / len(lst)

# Find all Prices Below 100
def FindPrice(lst):
    temp = []
    for s in lst:
        if (s < 100):
            temp.append(s)
    return temp


# Define Main Function
def Main():
        
    # Run the Header code so it displays at the top
    Header()
    
    # Create the List Variables
    names = ["Book ", "Tea  ", "Soda ", "Shoes", "Mug  ", "Tv   "]
    prices = [130.00, 153.00, 221.00, 117.00, 55.00, 200.00]
    disPrices = []
    sublist = []
    ids = [100, 101, 102, 103, 104, 105]
    
    # Print all of the Lists
    Space()
    PrintInfo(names, ids, prices)
    
    # Print the Price Average
    Space()
    print("=================- AVERAGES -==============")
    print("The Average Before The Discount is $", format(Average(prices), '.2f'))
    
    # Discount and Print Update
    disPrices = Discount(prices)
    Space()
    print("-")
    print("Prices Have Been Adjusted!")
    print("-")
    
    # Print Updated List
    Space()
    PrintInfo(names, ids, disPrices)
    
    # Print the Updated Price Average
    Space()
    print("=================- AVERAGES -==============")
    print("The Average After The Discount is $", format(Average(disPrices), '.2f'))    
    Space()
    
    # Find the Prices Below 100 Dollars
    sublist = FindPrice(disPrices)
    
    # Format Under 100 Prices
    Space()
    print("========- PRODUCTS UNDER <=  $100 -========")  
    print("     NAME     .     ID     .     PRICE     ")
    print("===========================================")
    # Print Under 100 Prices
    w = 0
    for z in sublist:
        print("    ", names[w], "        ", ids[w], "        ", format(sublist[w], '.2f'))
        w = w + 1        
    
    # End Main

# Call Main
Main()
        
# End Assignment