# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 06:31:36 2021

@author: Zac Shakespear
The purpose of this program is to assist in generating
timelines for fictional settings, particularly for
roleplaying. 

TO-DO:
"""

import pandas as pd
import random
import os

wd = os.getcwd()
wd+='\history.csv'

gen = pd.read_csv(wd)
randlimit = gen.size - 1

period = input("Enter the number of years for the timeline: ")
period = int(period)
numyears = input("Enter the start year for the timeline: ")
numyears = int(numyears)
it = input("Enter the number of years between each event: ")
it = int(it)
enddate = numyears + period

eventlist = pd.DataFrame(columns = ['Year', 'Event'])
while numyears < enddate:
    event = random.randint(0,randlimit)
    newevent = pd.DataFrame([[numyears, gen.at[event,'Events']]], 
                            columns = ['Year','Event'])
    eventlist = eventlist.append(newevent)
    numyears += it
    

with open("genHistory.txt", 'w') as file:
        textDummy = eventlist.to_string(header=True, index = False)
        file.write(textDummy)