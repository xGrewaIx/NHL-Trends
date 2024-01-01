# import all libraries
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np  
import csv 
#import os for managing files and directories
import os

# directory of where data is that we will use
directory = 'Standings_hits_PIMS_data'

# dictionary to store data from each CSV file
data_per_year = {}

for file in os.listdir(directory):
    if file.endswith('.csv'):
        year = file.split('_')[0]
        filepath = os.path.join(directory, file)
        df = pd.read_csv(filepath)
        data_per_year[year] = df
        
# print(data_per_year)

plt.style.use("classic")

# The first 2 for loops provide us with all the data points togethor
for year, df in data_per_year.items():
    plt.scatter(df['standing'], df['hitsFor'], marker = 'o', color = 'red')
    plt.xlabel("Standing")
    plt.ylabel("Hits For")
    plt.ylim([1500,6500])
    plt.title(f'Standings by Hits')
    
plt.show()
    
    

    
for year, df in data_per_year.items():
    plt.scatter(df['standing'], df['penalityMinutesFor'], marker = 'o', color = 'blue')
    plt.xlabel("Standing")
    plt.ylabel("penality Minutes for")
    plt.ylim([500,3000])
    plt.title(f'Standings by PIMS')
    
plt.show()


# These 2 for loops below provide data for each individual year 

for year, df in data_per_year.items():
    year2 = int(year)
    year3 = year2 + 1
    plt.scatter(df['standing'], df['hitsFor'], marker = 'o', color = 'orange')
    plt.xlabel("Standing")
    plt.ylabel("Hits For")
    plt.ylim([2000,5500])
    plt.title(f'Standings by Hits {year2} - {year3}')
    plt.show()


for year, df in data_per_year.items():
    year2 = int(year)
    year3 = year2 + 1
    plt.scatter(df['standing'], df['penalityMinutesFor'], marker = 'o', color = 'purple')
    plt.xlabel("Standing")
    plt.ylabel("penality Minutes for")
    plt.ylim([500,3000])
    plt.title(f'Standings by PIMS {year2} - {year3}')
    plt.show()  