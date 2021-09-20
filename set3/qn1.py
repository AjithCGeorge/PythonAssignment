# Qn1

import datetime

day=datetime.date.today().day
month=datetime.date.today().month
year=datetime.date.today().year
# print(datetime.date.today())
# print(day.value)
months31=[0,1,3,5,7,8,10,12]
print('today is : ',datetime.date(year,month,day) )
try:
    tomorrow=datetime.date(year,month,day+1)
except:
    tday=1
    try:
        tmonth=month+1
    except:
        tmonth=1
    tomorrow = datetime.date(year, tmonth, tday)
print('tomorrow is : ',tomorrow)
ymonth=month
yday=day-1
if day==1:
    if month-1 in months31:
        yday=31
        if month-1 ==0 :
            ymonth=1
            year=year-1
    else:
        if month-1 ==2:
            if year % 4 == 0 :
                if year % 100 == 0 and year % 400 !=0 :
                    yday=28
                else:
                    yday=29
        else:
            yday=30

print('Yesterday was    :',datetime.date(year,ymonth,yday))
