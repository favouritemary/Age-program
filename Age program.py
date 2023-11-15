#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Python programme to calculate age from date of birth

"""

import datetime, time

sec_min=60
sec_hour =60*sec_min
sec_day= sec_hour*24
sec_year= 365*sec_day

#Declaration of input variables#
b_year = int(input("Please enter the year of your birth, e.g. 1900-2023 :  "))
b_month = int(input("Enter the month of your birth, e.g. 1-12 :  "))
b_day= int(input("Enter the day of your birth, e.g. 1-31 : "))

# Date constructor to calculate date in sec from EPOCH time #

t= datetime.datetime(b_year, b_month , b_day)
age_sec = time.mktime(t.timetuple())
current_time = time.time()
curr_minus_birth = current_time - age_sec

#year, days, hours, minutes and seconds of event from EPOCH time

year_to_the_event =int(curr_minus_birth // sec_year)
year_to_the_event

days_event =int(curr_minus_birth%sec_year)//sec_day
days_event

a=(curr_minus_birth%sec_year)%sec_day
hour_event=int(a // sec_hour)
hour_event

min_event=int(a% sec_hour)//sec_min
min_event

event_sec=round((a%sec_hour)%sec_min)
event_sec

print  ( "Your birthday is ",b_day, t.strftime("%B"), b_year,        "(" "{0} years, {1} days, {2} hours, {3} minutes and {4} seconds ago"")"        .format(year_to_the_event,days_event,hour_event,min_event,event_sec))


# In[ ]:




