# import all libraries
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np  
import csv 
#import os for managing files and directories
import os

# use read_csv() from pandas to read each file
# Use for loops to go through all csv files efficently 

"""from line 14 to 23 are tests on how to obtain the certain data frame I wanted""" 

# mp_data_08_09 = pd.read_csv('C:/NHL-Trends/money_puck_data/2008-2009.csv')

# test to see if file is read in
# print(mp_data_08_09.head())

# use groupby to get specific data I want for each team, and use sum to add up all values

# hits_summary08_09 = mp_data_08_09.groupby("team")[["hitsFor", "penalityMinutesFor"]].sum()
# hits_summary08_09.to_csv("08to09_hits_PIMS_standings.csv",index=False)

# print(hits_summary08_09)

# To add standings/rank for each team in each year, I can scrape standings data
# Or I can manually insert them in excel which will update here 

"""Now create a for loop to go through all the csv files efficiently,
Will have to have 3 different loops due to lockouts and covid year,
these files are moved into the Standings_hits_PIMS_data folder"""

for year in range(2008, 2012):
    file_name = f'{year}-{year+1}.csv'
    file_path = "C:/NHL-Trends/money_puck_data/" + file_name
    data = pd.read_csv(file_path)
    
    summary = data.groupby("team")[["hitsFor", "penalityMinutesFor"]].sum()
    
    summary.to_csv(f'{year}_{year+1}_hits_PIMS_standings.csv')


for year in range(2013, 2019):
    file_name = f'{year}-{year+1}.csv'
    file_path = "C:/NHL-Trends/money_puck_data/" + file_name
    data = pd.read_csv(file_path)
    
    summary = data.groupby("team")[["hitsFor", "penalityMinutesFor"]].sum()
    
    summary.to_csv(f'{year}_{year+1}_hits_PIMS_standings.csv')
    
for year in range(2021, 2023):
    file_name = f'{year}-{year+1}.csv'
    file_path = "C:/NHL-Trends/money_puck_data/" + file_name
    data = pd.read_csv(file_path)
    
    summary = data.groupby("team")[["hitsFor", "penalityMinutesFor"]].sum()
    
    summary.to_csv(f'{year}_{year+1}_hits_PIMS_standings.csv')