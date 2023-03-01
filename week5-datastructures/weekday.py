# week 5 task
# day of the week program
# author: Audrey Fitzgerald

import datetime   # https://www.hellocodeclub.com/python-get-day-of-week

week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
week_num=datetime.date(2023,2,28).weekday()
print(week_days[week_num])

day = "Saturday"
if day == "Saturday":
      print("It is the weekend, yay!")
elif day == "Sunday":
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")











  




#import calendar

#week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
#weekday= calendar.weekday(2023,2,25)
#print(week_days[weekday])


#week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
#from calendar import weekday
#import datetime  
#dayofweek =input("What date is it? (in DD/MM/YYYY) ")  
#print(week_days[weekday])
#if("Saturday", "Sunday"):

    #print("It is the weekend yay!")
#else:
    #print("Yes, unfortunately today is a week_day")