# 2nd attempt to try and get the output if it is the weekend or weekday
# Author: Audrey Fitzgerald

import datetime   #https://pynative.com/python-get-the-day-of-week/

# given date
x_date = datetime.date(2023, 2, 27)
no = x_date.weekday()

if no < 5:
    print("Yes, unfortunately today is a weekday.")
else:  # 5 Sat, 6 Sun
    print("It is the weekend, yay!")
