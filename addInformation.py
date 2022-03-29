import numpy as np
import re
import calendar
import datetime
from datetime import date
import math
from FixDataBase import month_converter

def add_car(s_date,e_date):
    flag=0
    while(flag==0):
    
        print("\n-------------------------------------------------------------------\n")
        car_name=input("-Please select one of the cars above : ")
        car_name=car_name.capitalize()
        car_lic=input("-Please enter the selected car license : ")
        car_manYear=input("-Please enter the selected car  manufacturing year : ")

        if ((car_name+" with license = "+car_lic+" And with year of manufacturing the car = "+car_manYear) not in set_c):
            print("*ERROR : CAR SELECTED IS NOT AVAILABLR PLEASE RE-SELECT A CAR FROM THE ABOVE MENUE")
        
        else:
            flag=1

    customer_name=input("-Please enter the customer name : ")
    customer_name=customer_name.title()
    customer_id=input("-Please enter customer id : ")
    customer_dob=input("-Please enter customer date of birth : ")
    customer_num=input("-Please enter customer number : ")
    revenue=0
    numOfDays=0
    avg=0.0
    with open ('CarRentalCompleted.txt') as f:
            for line in f:
                car_info=line.split(";")
                if (car_info[4].lower()==car_lic.lower()):#check if the name and license of this
                    # line matches any item in the car_info_s list (which contains names and license of all cars)
                    f_=car_info[7].split(" ")
                    l=car_info[8].split(" ")
                    #function date format a given (day,month,year) into a 
                    #date form that is easier to do arithmetic operations to
                    f_date = date(int(f_[2]),month_converter(f_[1][0:3]),int(f_[0]))
                    l_date = date(int(l[2]),month_converter(l[1][0:3]),int(l[0]))
                    delta = l_date - f_date #calculates number of days between f_date and l-date
                    numOfDays+=delta.days
                    revenue+=int(car_info[9])
            numOfDays+=2
            avg=revenue/numOfDays #calculates the average price per day of a certain car
            
    
    f_=s_date.split(" ")
    l=e_date.split(" ")
    f_date = date(int(f_[2]),month_converter(f_[1][0:3].capitalize()),int(f_[0]))
    l_date = date(int(l[2]),month_converter(l[1][0:3].capitalize()),int(l[0]))    
    delta = l_date - f_date
    numOfDays=(delta.days)+2
    car_rentPrice=numOfDays*avg
    print(car_rentPrice,"=",numOfDays," * ",avg)
    print("\n-------------------------------------------------------------------\n") 

    dob_=customer_dob.split(' ')
    if ((customer_dob == dob_[0])):
            
            dob_=customer_dob.split('-')
                             #these lines are used to covert any format of dates into (day mothe year) format
            if (customer_dob==dob_[0]):
                dob_=customer_dob.split('/')
     
            dob_[1]=calendar.month_name[int(dob_[1])]  
            customer_dob=dob_[0]+" "+dob_[1]+" "+dob_[2]
    
    with open("CarRentalCompleted.txt", "a") as add:
        add.write(customer_name.title()+";"+customer_id+";"+customer_dob.title()+";"+customer_num+";"+car_lic.upper()+";"+car_name.title()
        +";"+car_manYear+";"+s_date.title()+";"+e_date.title()+";"+str(int(car_rentPrice))+"\n")
    

def add_information():

    print("--------------------------------------------------------")
    start_date=input(" -Please enter the car rent start date: ")
    end_date=input(" -Please enter the car rent end date: ")
    print("--------------------------------------------------------")
        
    #split the start and the end date into a list using space separator
    sd=start_date.split(" ") 
    ed=end_date.split(" ")

    global set_c
    set_c=set()
    set_NotAval=set()

    with open ('CarRentalCompleted.txt') as f:
        for line in f:
            car_info=line
            data_c=car_info.split(";") #split each line into a list using ';' separator
            data_cs=data_c[7].split(" ")
            data_ce=data_c[8].split(" ")
            #datetime class is used to make it easy to do arithmetic operation on dates 
            arg_s=datetime.datetime(int(sd[2]),month_converter(sd[1][0:3]),int(sd[0]))
            arg_cs=datetime.datetime(int(data_cs[2]),month_converter(data_cs[1][0:3]),int(data_cs[0]))
            arg_e=datetime.datetime(int(ed[2]),month_converter(ed[1][0:3]),int(ed[0]))
            arg_ce=datetime.datetime(int(data_ce[2]),month_converter(data_ce[1][0:3]),int(data_ce[0]))

            #this if statement is true if the dates entered by the user are outside the range of this line's dates
            if((((arg_s<arg_cs)and(arg_e<arg_cs))or((arg_s>arg_ce)and(arg_e>arg_ce)))and(data_c[5]+";"+data_c[4] not in set_NotAval)):
                 
                 set_c.add(data_c[5]+" with license = "+data_c[4]+" And with year of manufacturing the car = "+data_c[6])

            elif((data_c[5]+" with license = "+data_c[4]+" And with year of manufacturing the car = "+data_c[6]) in set_c):

                 set_c.remove((data_c[5]+" with license = "+data_c[4]+" And with year of manufacturing the car = "+data_c[6]))
                 set_NotAval.add(data_c[5]+";"+data_c[4])  

            else:

                 set_NotAval.add(data_c[5]+";"+data_c[4])       
                 
    if(len(set_c)!=0):

        print("\n  **cars available during these dates**  \n")
        for x in set_c:
            print(x)
            print("\n")

        #call the add_car() function to add the information about the customer and the selected car    
        add_car(start_date,end_date);
    
    else:
        print("\n No cars are available during these dates.")
               
    return
