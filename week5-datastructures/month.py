#creating tuples
# tuples have round brackets
# tuples are like lists but you can't set or append them
# Author: Audrey Fitzgerald

months =("January",  #first tuple with all the months of the year
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"
)
summer = months[4:7]  #expected output is May, June and July as tuple starts at 0.   # 2nd tuple is just the months from 4 to 7
for month in summer:
    print(month)