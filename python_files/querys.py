import pyodbc 
import pandas as pd
import csv


conn = pyodbc.connect(driver='{SQL Server}', server='(local)', database='NHLTrends',               
               trusted_connection='yes')

cursor = conn.cursor()

query = "SELECT * FROM year_hits_pims_standing"

# Create a dataframe with all data
df = pd.read_sql(query, conn)

# Print first 20 rows
print(df.head(20))
