import numpy as np
import re
import calendar
import datetime
from datetime import date
import math
from FixDataBase import month_converter

#-----------------------------------------   Task 4   --------------------------------------------------------------------
def print_each_car_info():
    car_info_s=set()
    numOfDays=0
    revenue=0
    avg=0.0
    with open ('CarRentalCompleted.txt') as f:
        for line in f:
            car_info=line.split(";")#split lines in the completedEntries text file into a list using ';' separator 
            car_info_s.add(car_info[4]+";"+car_info[5])#add the car name and it's license to the car_info_s list
    
    print(" **statistics about each car in the database**")
    print("\n--------------------------------------------------------------------------------------------------------------------------------\n")
    
    for k in car_info_s:
        info_s=k.split(";")
        with open ('CarRentalCompleted.txt') as f:
            for line in f:
                car_info=line.split(";")
                if ((car_info[4]+";"+car_info[5])==(k)):#check if the name and license of this
                    # line matches any item in the car_info_s list (which contains names and license of all cars)
                    f_=car_info[7].split(" ")
                    l=car_info[8].split(" ")
                    #function date format a given (day,month,year) into a 
                    #date form that is easier to do arithmetic operations to
                    f_date = date(int(f_[2]),month_converter(f_[1][0:3].capitalize()),int(f_[0]))
                    l_date = date(int(l[2]),month_converter(l[1][0:3].capitalize()),int(l[0]))
                    delta = l_date - f_date #calculates number of days between f_date and l-date
                    numOfDays+=delta.days
                    revenue+=int(car_info[9])
            numOfDays+=2
            avg=revenue/numOfDays #calculates the average price per day of a certain car
            print("  | -Number of days "+info_s[1]+" | with license : "+info_s[0]+" | was rented = ",numOfDays," days "+" | Revenue made = "
            ,revenue," | Average price/day = ",round(avg,3),"\n")
            numOfDays=0
            revenue=0
            avg=0.0
    print("\n----------------------------------------------------------------------------------------------------------------------------------\n")
    return

#--------------------------------------------------------END OF TASK 4--------------------------------------------------------------------------------------------------------
