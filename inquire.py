import numpy as np
import re
import calendar
import datetime
from datetime import date
import math


def printInfoId():
    print("\n----------------------------------------------------------------------------------------\n")
    read_name=input(" -Please enter the name of the person you want to search for or his/her ID:")
    set1=set()
    Tsum=0
    with open ('CarRentalCompleted.txt') as f:
        flag=0
        c_name=""
        for line in f: #loops at each line in the CarRentalCompleted text file
            car_info=line.split(";") #split the read line into a list using ';' separator 
            #this if statement is true when car_info[0] (which is the name item of the split line ) or 
            #car_info[1] (which is the id item  of the split line) matches the string entered by the user
            if car_info[0].lower() == read_name.lower() or car_info[1] == read_name :
                if(flag==0):
                    print("\n info: "+car_info[0]+" | Id: "+car_info[1]+" | Date of birth: "+car_info[2]+" | phone number: "+car_info[3])
                    c_name=car_info[0]
                    flag=1 #this variable is used to make the above if statement false so that 
                    #the person's info would be printed only once 
                #add the car info to the set 
                set1.add(car_info[5]+" | With license: "+car_info[4]+" | Start date: "+car_info[7]+" | End date: "+car_info[8]+
                " | price= "+car_info[9])
                Tsum+=int(car_info[9],10)

    #this if statement is true when the set is empty and Tsum vaiable equals zero
    if(len(set1)==0 and Tsum==0):
        print("\n **Error: No one with that name rented any car here")

    else: 
        print("\n "+c_name+" rented : ")     
        for k in set1:
            print("\n ==> ",k)
        print("\n"+" "+c_name+" paid : ",Tsum)
 
    print("\n----------------------------------------------------------------------------------------\n")
    return      



def printInfoCl():
    print("\n----------------------------------------------------------------------------------------\n")
    read_cl=input(" Please enter the car license number:")
    set1=set()
    Tsum=0
    c_name=""
    with open ('CarRentalCompleted.txt') as f:
        flag=0
        for line in f:#loops at each line in the completedEntries text file
            car_info=line.split(";") #split the read line into a list using ';' separator 
            #this if statement is true when car_info[4] (which is the liscens item of the split line ) 
            # matches the string entered by the user
            if car_info[4].lower() == read_cl.lower():
                if(flag==0):
                    print("\n CL: "+car_info[4]+"| CM: "+car_info[5]+"| Year: "+car_info[6])
                    c_name=car_info[5] 
                    flag=1
                set1.add(car_info[0]+" | id: "+car_info[1]+" | Start date: "+car_info[7]+" | End date: "+car_info[8]+" | price = "+car_info[9])
                Tsum+=int(car_info[9],10)       
            
    if(len(set1)==0 and Tsum==0):
        print("\n **Error: No one rented a car with license : "+read_cl)

    else:        
        print("\n People who rented "+c_name+" with license : "+read_cl)   
        for k in set1:       
            print("\n ==> ",k)  
        print("\n"+"  revenue made by renting this: ",Tsum)
        print("\n----------------------------------------------------------------------------------------\n")
    return    