from FixDataBase import * 
from inquire import *
from  addInformation import *
from carStatistics import *

fixEntries();
removeDuplicate();

print("\n")
print(" -----------------------------------------------------------------") 
print(" | -Press 1 to Inquiry about a person using his/her Name or Id.  |")
print(" | -Press 2 to Inquiry about a person using car license.         |")
print(" | -Press 3 to Add a car and it's rental information.            |")
print(" | -Press 4 to print statistics about each car.                  |")
print(" | -Press 5 to exit.                                             |")
print(" -----------------------------------------------------------------\n")

op=input("==> ")

while op!='5':
    
    if (op=='1'):
        printInfoId(); 
    
    elif(op=='2'):
        printInfoCl();
   
    elif(op=='3'):
        add_information();

    elif(op=='4'):
        print_each_car_info();
    
    elif(op=='5'):
        exit(1)

    else:
        print("\n ERROR: Please enter a valid option from the menue below e.g(1 or 2 or 3 or 4 or 5)\n")

    print("\n")
    print(" -----------------------------------------------------------------")
    print(" | -Press 1 to Inquiry about a person using his/her Name or Id.  |")
    print(" | -Press 2 to Inquiry about a person using car license.         |")
    print(" | -Press 3 to Add a car and it's rental information.            |")
    print(" | -Press 4 to print statistics about each car.                  |")
    print(" | -Press 5 to exit.                                             |")
    print(" -----------------------------------------------------------------")
    op=input("==> ")
