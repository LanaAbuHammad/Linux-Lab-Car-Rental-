import numpy as np
import re
import calendar
import datetime
from datetime import date
import math

def readData():
    #open CarRentalOld text file to read and write data
    op=open("CarRentalOld.txt","r+")
    global counter
    counter=0
    
    with open ('CarRentalOld.txt') as f:
        
        for line in f:
           counter+=1 #this counter counts number of lines in the CarRentalOld.txt file

    counter+=1
    global data 
    data= np.empty(counter, dtype=np.object) #this code craete an array of empty lists 
    for i in range(data.shape[0]):
         data[i] = []
         data[i].append(i) # appending empty list (data[i]) 
 
    i=0   

    with open ('CarRentalOld.txt') as f:
        for line in f: #this code is usefull to loop at evrey line in the CarRentalOld.txt file
           str=line
           data2=str.split(";") #split each line into a list (data2) using ';' separator
           # these lines are used to add items to the list 
           data[i].append(data2[0]) #adds name
           data[i].append(data2[1]) #adds id
           data[i].append(data2[2]) #adds date of birth
           data[i].append(data2[3]) #adds number
           data[i].append(data2[4]) #adds car license
           data[i].append(data2[5]) #adds car name
           data[i].append(data2[6]) #adds car manufacturering year
           data[i].append(data2[7]) #adds start date
           data[i].append(data2[8]) #adds end date 
           data2[9] = re.sub(r'\n',"", data2[9]) #remove '\n' from the price item
           data[i].append(data2[9]) #adds price
       
           i+=1
    op.close(); #close CarRentalInfo file stream

#this function is used to check wether or not a giver number is in the char_index list
def check(num):
    return(num not in  char_index) 

def modifyDate():
    global chgdate
    chgdate=0
    for i in range(counter-1): #loops counter-1 times (number of lines in the file)
        
        b_date=data[i][3].split(' ') #split birth of date in each line using space as a separator
        s_date=data[i][8].split(' ') #split start date in each line using space as a separator
        e_date=data[i][9].split(' ') #split end date in each line using space as a separator
        #this if statement is true when data[i][3] item is not empty and it is not written in (day month year) format 
        if ((data[i][3] != '') and (data[i][3] == b_date[0])):
            
            b_date=data[i][3].split('-') #split date of birth  using '-' as a separator

            if (data[i][3]==b_date[0]): #this if statement is true if data[i][3] item is not written in (day-month-year) format

                b_date=data[i][3].split('/') #split date of birth using '/' as a separator into a list

            b_date[1]=calendar.month_name[int(b_date[1])] #convert month from int format to string e.g( 3 ==> March)
            data[i][3]=b_date[0]+" "+b_date[1].capitalize()+" "+b_date[2] #reconcatenate date format into (day month year) 
            chgdate+=1
        #this if statement is true when data[i][8] item is not empty and it is not written in (day month year) format 
        if ((data[i][8] != '') and (data[i][8] == s_date[0])):
            
            s_date=data[i][8].split('-') #split the start date using '-' as a separator

            if (data[i][8]==s_date[0]):#this if statement is true if data[i][8] item is not written in (day-month-year) format

                s_date=data[i][8].split('/') #split the start date using '/' as a separator
     
            s_date[1]=calendar.month_name[int(s_date[1])]  
            data[i][8]=s_date[0]+" "+s_date[1].capitalize()+" "+s_date[2]
            chgdate+=1
       
        #this if statement is true when data[i][9] item is not empty and it is not written in (day month year) format 
        if ((data[i][9] != '') and (data[i][9] == e_date[0])):
            
            e_date=data[i][9].split('-') #split the end day using '-' as a separator

            if (data[i][9]==e_date[0]):#this if statement is true if data[i][9] item is not written in (day-month-year) format

                e_date=data[i][9].split('/')#split the end date  using '/' as a separator
     
            e_date[1]=calendar.month_name[int(e_date[1])]  
            data[i][9]=e_date[0]+" "+e_date[1].capitalize()+" "+e_date[2]
            chgdate+=1
    return

def fixEntries():
    #call readData function to store the data on the CarRentalInfo text file into an array list
    readData();
    #open files to write on them
    complete=open("CarRentalOld.txt","w") 
    missing=open("CarRentalMissing.txt","w")
    #call modifyDate function to fix date items of the list
    modifyDate();
    errors=[0,0,0,0,0,0,0]
    fixed=[0,0,0,0,0,0,0]
    ndroppentry=0
    for i in range(counter-1):

        global char_index
        char_index=[]
        index_counter=0
        
        while True:
            
            try:
                 
                index_counter=data[i].index('',index_counter) #search for index of an empty string '' and return its value
                char_index.append(index_counter) #add index to index_conter list
                index_counter+=1
        
             
            except ValueError as e:
                break; #break when index is out of range
        
        for e in range(len(char_index)):
            if(char_index[e]<=7 and len(char_index)==1):
                errors[char_index[e]-1]+=1
            
        #this if statement is true when there is no missing entries in the i'th list 
        if (len(char_index) == 0): 
            #add this completed list to the completeEntries
            complete.write(data[i][1]+";"+data[i][2]+";"+data[i][3]+";"+data[i][4]+";"+data[i][5]+
            ";"+data[i][6]+";"+data[i][7]+";"+data[i][8]+";"+data[i][9]+";"+data[i][10]+"\n")
            continue;

        #this if statement is true when the start date and the end date are missing from the i'th list
        elif(((check(8) and check(9)) == False)):
            #this list is added to the missingEntries text file because if the start and the end
            #  dates are missing we can't fix the information 
            missing.write(data[i][1]+";"+data[i][2]+";"+data[i][3]+";"+data[i][4]+";"+data[i][5]+
            ";"+data[i][6]+";"+data[i][7]+";"+data[i][8]+";"+data[i][9]+";"+data[i][10]+"\n")
            continue;
        
        #this if statement is true when the name and id and number and the license are missing from the i'th list
        elif(((check(1) or check(2) or check(4)) == False)):
             #this list is added to the missingEntries text file because the information can't be fixed 
            missing.write(data[i][1]+";"+data[i][2]+";"+data[i][3]+";"+data[i][4]+";"+data[i][5]+
            ";"+data[i][6]+";"+data[i][7]+";"+data[i][8]+";"+data[i][9]+";"+data[i][10]+"\n")
            ndroppentry+=1
            continue;
                 
        else:                   
            for k in range(counter-1):
                 flag_in=0
                 if(data[i][1]!='' or data[i][2]!='' or data[i][4]!=''):
                     flag_in=1
                     if((data[k][1]==data[i][1] and data[k][1]!='')or(data[k][2]==data[i][2] and data[k][2]!='')or
                     (data[k][4]==data[i][4] and data[k][4]!='')):
                         if(data[i][1]=='' and data[k][1]!=''):
                             data[i][1]=data[k][1]
                         if(data[i][2]=='' and data[k][2]!=''):
                             data[i][2]=data[k][2]
                         if(data[i][3]=='' and data[k][3]!=''):
                             data[i][3]=data[k][3]
                         if(data[i][4]=='' and data[k][4]!=''):
                             data[i][4]=data[k][4]

                 if(data[i][5]!='' and data[k][5]!=''):
                     flag_in=1
                     if(data[k][5]==data[i][5]):
                         if(data[i][6]==''):
                             data[i][6]=data[k][6]
                         if(data[i][7]==''):
                             data[i][7]=data[k][7]
                 if(flag_in==0):
                     break

            flag=1
            for n in range(1,11):
                if(data[i][n]==''):
                    flag=0          
          
            if(flag==1):
                for f in range(len(char_index)):
                    if(char_index[f]<=7):
                        fixed[char_index[f]-1]+=1  
                   
                complete.write(data[i][1].title()+";"+data[i][2]+";"+data[i][3].title()+";"+data[i][4]+";"+data[i][5]+";"
                +data[i][6]+";"+data[i][7]+";"+data[i][8].title()+";"+data[i][9].title()+";"+data[i][10]+"\n") 

                
        if flag==0:
           
            for k in range(counter-1):
                  k_str=""
                  i_str=""

                  if(data[k]==data[i]):
                      continue;

                  elif '' in data[k]:
                      flag_in=0
                      for n in char_index:
                          if (data[k][n]==''):
                              flag_in=1
                              break
                      if(flag_in==1):
                           continue; 
                      else:

                          for c in range(1, 11):
                              if c not in char_index:
                                  if(data[k][c]!=''):
                                      k_str=k_str+data[k][c]+";"
                                      i_str=i_str+data[i][c]+";"

                          if(k_str==i_str):
                              for n in char_index:
                                  data[i][n]=data[k][n]
                              for f in range(len(char_index)):
                                  if(char_index[f]<=7):
                                       fixed[char_index[f]-1]+=1  
                              
                              complete.write(data[i][1].title()+";"+data[i][2]+";"+data[i][3].title()+";"+data[i][4]+";"+data[i][5]+";"
                              +data[i][6]+";"+data[i][7]+";"+data[i][8].title()+";"+data[i][9].title()+";"+data[i][10]+"\n") 
                              flag=1
                              break;
                  
                  else:
                   
                      for c in range(1, 11):
                          if c not in char_index:
                              k_str=k_str+data[k][c]+";"
                              i_str=i_str+data[i][c]+";"

                      if(k_str==i_str):
                          for f in range(len(char_index)):
                               if(char_index[f]<=7):
                                   fixed[char_index[f]-1]+=1  
                          
                          complete.write(data[k][1].title()+";"+data[k][2]+";"+data[k][3].title()+";"+data[k][4]+";"+data[k][5]+";"
                          +data[k][6]+";"+data[k][7]+";"+data[k][8].title()+";"+data[k][9].title()+";"+data[k][10]+"\n") 
                          flag=1
                          break;      
            if flag==0:
                missing.write(data[i][1]+";"+data[i][2]+";"+data[i][3]+";"+data[i][4]+";"+data[i][5]+";"+data[i][6]+";"+
                data[i][7]+";"+data[i][8]+";"+data[i][9]+";"+data[i][10]+"\n")


    print("\n")
    print("           ***Summary of data missing from the database***                   ")
    print(" Number of entries with wrong date format in the database = ",chgdate)
    print(" Number of entries where names are dropped from the database = ",errors[0])
    print(" Number of entries where Ids are dropped from the database = ",errors[1])
    print(" Number of entries where dob are dropped from the database = ",errors[2])
    print(" Number of entries where mobile numbers are dropped from the database = ",errors[3])
    print(" Number of entries where personal entry can not be completed = ",ndroppentry)
    print(" Number of entries where car make are dropped from the database = ",errors[5])
    print(" Number of entries where car Ids are dropped from the database = ",errors[4])
    print(" Number of entries where car models (year) are dropped from the database = ",errors[6])
    print("\n")
    print("           ***Summary of data recovered from the database***                   ")
    print(" Number of entries with wrong date format fixed in the new database = ",chgdate)
    print(" Number of entries where names recovered in the new database = ",fixed[0])
    print(" Number of entries where Ids recovered in the new database = ",fixed[1])
    print(" Number of entries where dob recovered in the new database = ",fixed[2])
    print(" Number of entries where mobile numbers recovered in the database = ",fixed[3])
    print(" Number of entries where car make recovered in the database = ",fixed[5])
    print(" Number of entries where car models (year) recovered in the database = ",fixed[6])
    
    complete.close();
    missing.close();
    return  
         
def removeDuplicate():
    wduplicate=0
    global nduplicate
    nduplicate=0
    lines_dup = set() # holds lines already seen
    for line in open("CarRentalOld.txt", "r"):
        wduplicate+=1

    with open("CarRentalCompleted.txt", "w") as removed_dup:
	    for line in open("CarRentalOld.txt", "r"):
	        if line.lower() not in lines_dup:#check if line is not duplicate
	            removed_dup.write(line.title()) 
	            lines_dup.add(line.lower())#add this line to the lines_dup set

    for line in open("CarRentalCompleted.txt", "r"):
        nduplicate+=1           

    nduplicate=wduplicate-nduplicate  
    print(" Number of duplicate entries removed from the new database = ",nduplicate)
    return

#function for converting month from int to string e.g( March ==> 3 )
def month_converter(month):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months.index(month) + 1

#-----------------------------------------END OF TASK 1---------------------------------------------------------------------------
