#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

import pandas as pd

# read file as dataframe
football = pd.read_csv('/users/emilyrobinson/Dropbox/metis/prework/dsp/python/football.csv')
    
# create a function that returns absolute difference in goals
def dif_goals(x):
    return abs(x['Goals Allowed'] - x['Goals'])

# apply function to football dataframe
difference_in_goals = football.apply(dif_goals, axis = 1)

# find the index of the minimum  
index_min = difference_in_goals.idxmin()

# find the team at the index of the minimum 
print football['Team'][index_min]
