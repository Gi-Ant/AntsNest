"""
Author: Ramkumar NJ
~~~~~~~~~~~~~~~~~~~
Problem: To find out the day of any given date
Functional Requirement: I need to get the day of the week for any date I provide as input in the format DD-MM-YYYY
                        - it can be as back dated as 1-1-0001 or future date like 31-12-9999
Users: Anyone who want to know the day of a date
Target: Windows 7,8,10
Interface: command-line
Inputs: Date for which I want the date will be given as input. 
        The date is given in DD-MM-YYYY or D-M-YYYY format. The delimiter can be - or / or : or . or ,
Maintainer: ramkumar.nj@gmail.com
"""

#Get current date and day
from datetime import datetime, date, time

def dayOFdaynum(daynum):
    if daynum == 0:
        day='Monday';
    elif daynum == 1:
        day='Tuesday';
    elif daynum == 2:
        day='Wednesday';
    elif daynum == 3:
        day='Thursday';
    elif daynum == 4:
        day='Friday';
    elif daynum == 5:
        day='Saturday';
    elif daynum == 6:
        day='Sunday';
    return (day);

dt = datetime.now();
tt = dt.timetuple();

DayToday = dayOFdaynum(tt[6]);

dd=tt[2];
mm=tt[1];
yyyy=tt[0];
todaynum=tt[6];

today = str(dd)+'-'+str(mm)+'-'+str(yyyy)+', '+DayToday;
print("\nToday is %s\n" %(today));

while(1):
    tgtdaynum=todaynum;
    while(1):
        tgtdate = input("Enter the date [DD-MM-YYYY] or \"Done\" to Quit: ")
        if(tgtdate.upper() == "DONE"):
            exit();
        temp_tgtdate = tgtdate.split('-');
        if (len(temp_tgtdate) != 3):
            temp_tgtdate = tgtdate.split('/');
            if (len(temp_tgtdate) != 3):
                temp_tgtdate = tgtdate.split(':');
                if (len(temp_tgtdate) != 3):
                    temp_tgtdate = tgtdate.split(',');
                    if (len(temp_tgtdate) != 3):
                        temp_tgtdate = tgtdate.split('.');
        try:
            tgtdd=int(temp_tgtdate[0]);
            tgtmm=int(temp_tgtdate[1]);
            tgtyyyy=int(temp_tgtdate[2]);
            if((tgtmm==2 and tgtyyyy%4==0 and tgtdd > 29) 
            or (tgtmm==2 and tgtyyyy%4 !=0 and tgtdd>28) 
            or ((tgtmm==4 or tgtmm==6 or tgtmm==9 or tgtmm==11) and tgtdd>30) 
            or tgtdd > 31 or tgtdd < 1 
            or tgtmm < 1 or tgtmm > 12):
                print("\nEnter a valid date!\n");
            else:
                break;
        except:
            print("\nEnter a valid date in DD-MM-YYYY format!\n");

    if (dd==tgtdd and mm==tgtmm and yyyy==tgtyyyy):
       print("Today is a %s-%s-%s, %s\n" %(tgtdd,tgtmm,tgtyyyy,DayToday));
    elif (tgtyyyy > yyyy) or (tgtyyyy == yyyy and mm < tgtmm) or (tgtyyyy == yyyy and mm == tgtmm and dd <tgtdd):
        idxyyyy = yyyy;
        idxmm = mm;
        idxdd = dd;
        while (idxyyyy <= tgtyyyy):
            while(idxmm <= 12):
    #            print("Month: %i" %(idxmm));
                if(idxmm == 1 or idxmm == 3 or idxmm == 5 or idxmm == 7 or idxmm == 8 or idxmm == 10 or idxmm == 12): dayend = 31;
                elif(idxmm == 2):
                    if(idxyyyy%4 == 0): dayend = 29;
                    else: dayend = 28;
                elif(idxmm == 4 or idxmm == 6 or idxmm == 9 or idxmm == 11): dayend = 30;
                while(idxdd <= dayend):
    #               print("Day: %i" %(idxdd));
                    if(idxdd == tgtdd and idxmm == tgtmm and idxyyyy == tgtyyyy):
                        tgtday = tgtdaynum;
    #                   print("Value %i" %(tgtday));
                        day = dayOFdaynum(tgtday);
                        print("%i-%i-%i is a %s\n" %(tgtdd,tgtmm,tgtyyyy,day));
                        break;
                    #else:
                    idxdd += 1;
                    tgtdaynum += 1;
                    if (tgtdaynum == 7):
                        tgtdaynum = 0;
                idxmm += 1;
                idxdd = 1;
            idxyyyy +=1;
            idxmm = 1;
    else:
        idxyyyy = yyyy;
        idxmm = mm;
        idxdd = dd;
        while (idxyyyy >= tgtyyyy):
            while(idxmm >= 1):
    #            print("Month: %i" %(idxmm));
                if(idxmm == 1 or idxmm == 3 or idxmm == 5 or idxmm == 7 or idxmm == 8 or idxmm == 10 or idxmm == 12): dayend = 31;
                elif(idxmm == 2):
                    if(idxyyyy%4 == 0): dayend = 29;
                    else: dayend = 28;
                elif(idxmm == 4 or idxmm == 6 or idxmm == 9 or idxmm == 11): dayend = 30;
                while(idxdd >= 1):
    #                print("Day: %i" %(idxdd));
                    if(idxdd == tgtdd and idxmm == tgtmm and idxyyyy == tgtyyyy):
                        tgtday = tgtdaynum;
    #                    print("Value %i" %(tgtday));
                        day = dayOFdaynum(tgtday);
                        print("%i-%i-%i is a %s\n" %(tgtdd,tgtmm,tgtyyyy,day));
                        break;
                    #else:
                    idxdd -= 1;
                    tgtdaynum -= 1;
                    if (tgtdaynum == -1):
                        tgtdaynum = 6;
                idxmm -= 1;
                if(idxmm == 1 or idxmm == 3 or idxmm == 5 or idxmm == 7 or idxmm == 8 or idxmm == 10 or idxmm == 12): dayend = 31;
                elif(idxmm == 2):
                    if(idxyyyy%4 == 0): dayend = 29;
                    else: dayend = 28;
                elif(idxmm == 4 or idxmm == 6 or idxmm == 9 or idxmm == 11): dayend = 30;
                idxdd = dayend;
            idxyyyy -=1;
            idxmm = 12;
