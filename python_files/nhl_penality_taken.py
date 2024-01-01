# import all libraries
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np  
import csv 
#import os for managing files and directories
import os


# add file name where data is
directory = 'money_puck_data'

#PIMS is column 35

penalty_data = pd.DataFrame({'Year':
    ['08-09', '09-10', '10-11', '11-12', '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '21-22', '22-23'],
    'Total PIMS': [0]*12})

current_year_index = 0

for file in os.listdir(directory):
    if file.endswith('.csv'):
        file_path = os.path.join(directory, file)
        data = pd.read_csv(file_path)
        total_PIMS = data.iloc[:, 35].sum()
        # Update the 'Total PIMS' column for the current year
        penalty_data.at[current_year_index, 'Total PIMS'] += total_PIMS
        # Move to the next year for the next file
        current_year_index += 1
        
## test to see if data prints 
print(penalty_data)

# the below code that has been commented out is the PIMS_per_year plot in figures

PIMS_per_year = plt.plot(penalty_data['Year'], penalty_data['Total PIMS'], marker='o') # Line plot with markers at each data point
plt.title('Total PIMS by Year') # Title of the graph
plt.xlabel('Year') # Label for the x-axis
plt.ylabel('Total PIMS') # Label for the y-axis
plt.annotate('Vegas Expansion',xy=('17-18',39616),
             xytext=('16-17',43000),
             arrowprops=dict(facecolor="gold",shrink=0.05))
plt.annotate('Seattle Expansion',xy=('21-22',41380),
             xytext=('17-18',47000),
             arrowprops=dict(facecolor="Teal",shrink=0.05))
plt.xticks(rotation=45) # Rotate the x-axis labels to make them readable
plt.tight_layout() # Adjust the layout so everything fits without overlapping
plt.show() # Display the plot
