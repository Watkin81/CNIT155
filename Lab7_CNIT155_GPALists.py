#====================================================================================
# Jake Watkins, Thursday 11:30am
# Watkin81@purdue.edu
# lalalalalallllalala
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
    print("*                CNIT155 Lab 8            *")
    print("*                                         *")
    print("*                     GPA                 *")
    print("*******************************************")
    Space()
    
# Since I need line spaces in this program, this will save time
def Space():
    print("")
    

# Define Main Function
def Main():
        
    # Run the Header code so it displays at the top
    Header()
    
    # Ask for List Length User Input and Define Variables
    length = int(input("How many Students are there in your Class?: "))
    count = 0
    name = []
    gpa = []
    
    # Get List Inputs from User
    while count < length:
        # Get Name and Append to Name List
        temp = input("Input Sudent #"+str(count+1)+" Name: ")
        name.append(temp)
        while True:
            # Get User GPA Value and Compare to Allowed Values
            temp2 = float(input("Input Sudent #"+str(count+1)+" GPA: "))
            if ((temp2 >= 0) and (temp2 <= 4.0)):
                # Good GPA, Add to List
                gpa.append(temp2)
                count = count + 1
                break
            else:
                # Bad GPA, Ask for Input Again and Give Error
                print ("The GPA Must be Between 0 and 4.0 (Both Inclusive!)")
                Space()
                continue
    Space()
    print("================ LIST ================")
    print("\tName\t\tGPA")
    print("       -------         ------- ")
    coun = 0
    while coun < len(name):
        print("\t"+name[coun]+"\t\t", gpa[coun])
        coun = coun + 1

    
    # Gather the GPA Information
    sum = 0
    for t in gpa:
        sum = sum + t
        
    avg = sum / len(gpa)
    maximum = max(gpa)
    minimum = min(gpa)
    
    # Print the GPA Information
    Space()
    print("=========================================")
    print ("The Average of the GPAs is ", "{:0.2f}".format(avg))
    print ("The Highest GPA is ", "{:0.2f}".format(maximum))
    print ("The Lowest GPA is ", "{:0.2f}".format(minimum))
    print("=========================================")
    
    # End Main

# Call Main
Main()
        
# End Assignment