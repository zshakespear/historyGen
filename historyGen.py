# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 06:31:36 2021

@author: Zac Shakespear
The purpose of this program is to assist in generating
timelines for fictional settings, particularly for
roleplaying. 

TO-DO:
    Allow user to set start year
    Allow user to set number of years per event
    Random number of years between events
"""

import pandas as pd
import random

gen = pd.read_csv('c://Users/zacos/Desktop/history.csv')
randlimit = gen.size - 1

period = input("Enter the number of years for the timeline: ")
period = int(period)
numyears = input("Enter the start year for the timeline: ")
numyears = int(numyears)
enddate = numyears + period

eventlist = pd.DataFrame(columns = ['Year', 'Event'])
while numyears < enddate:
    event = random.randint(0,randlimit)
    newevent = pd.DataFrame([[numyears, gen.at[event,'Events']]], 
                            columns = ['Year','Event'])
    eventlist = eventlist.append(newevent)
    numyears += 1
    

with open("genHistory.txt", 'w') as file:
        textDummy = eventlist.to_string(header=True, index = False)
        file.write(textDummy)