# import all libraries
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np  
import csv 
#import os for managing files and directories
import os

### hits for column is column 37

# add file name where data is
directory = 'money_puck_data'

## First we are analyzing how much hitting has increased or decreased over
## the years as the general consesnous is that hitting has decreased
# create a new dataframe where we will keep the hiting data 
hitting_data = pd.DataFrame({'Year':
    ['08-09', '09-10', '10-11', '11-12', '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '21-22', '22-23'],
    'Total Hits': [0]*12})

current_year_index = 0

for file in os.listdir(directory):
    if file.endswith('.csv'):
        file_path = os.path.join(directory, file)
        data = pd.read_csv(file_path)
        total_hits = data.iloc[:, 37].sum()
        # Update the 'Total Hits' column for the current year
        hitting_data.at[current_year_index, 'Total Hits'] += total_hits
        # Move to the next year for the next file
        current_year_index += 1
        
## test to see if data prints 
print(hitting_data)

# the below code that has been commented out is the hits_per_year plot in figures
plt.style.use("classic")

hits_per_year = plt.plot(hitting_data['Year'], hitting_data['Total Hits'], marker='o') # Line plot with markers at each data point
plt.title('Total Hits by Year') # Title of the graph
plt.xlabel('Year') # Label for the x-axis
plt.ylabel('Total Hits') # Label for the y-axis
plt.annotate('Vegas Expansion',xy=('17-18',109746),
             xytext=('17-18',105000),
             arrowprops=dict(facecolor="gold",shrink=0.05))
plt.annotate('Seattle Expansion',xy=('21-22',120372),
             xytext=('17-18',122500),
             arrowprops=dict(facecolor="Teal",shrink=0.05))
plt.xticks(rotation=45) # Rotate the x-axis labels to make them readable
plt.tight_layout() # Adjust the layout so everything fits without overlapping
plt.show() # Display the plot





"""
This is an example I had used to loop through mutiple csv files

https://stackoverflow.com/questions/45947887/python-looping-through-csv-files-and-their-columns


for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        if filename in filename:
            numFiles.append(filename)
            
for i in numFiles:
    file = open(os.path.join(directory, i), "rU")
    reader = csv.reader(file, delimiter=',')
    for column in reader:
        print(column[37])
""" 
