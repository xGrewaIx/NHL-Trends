# NHL-Trends

## Information about what this repository

This repository showcases my ongoing work in the analysis of how ice hockey has evolved since data has been tracked (2008-2009). Later on I will dive into each Stanley Cup winning team and try to find common attributes amongst Stanley Cup winning teams

*Data from the lockout (2012-2013) and the Covid Seasons (2019-2020 and 2020-21)were not used due to the inconsistency in games played as a full 82 game regular season was not completed during these years*

**Data was obtained from Money Puck (https://moneypuck.com/teams.htm)**

## Findings

- We see that the average number of hits per team was on a steady increase from 2008 to 2015 where it then went on a downward trend, whereas penalty minutes remained on a steady decrease over the years.

- In the next queries we find that there were 102 nhl teams that were above average in both hits and penalty minutes, and out of those teams 48 made the playoffs. Based off this I beleived there was not a strong correlation between hits, penalty minutes and standing.

- To back up my belief above I created a linear model with standing as the response variable with hits and pims as the predictor variables. When I check the diagnostic plots I see that the conditions for a linear regression are not satisfied therefore we do not continue on with this analysis.

## What each folder contains

- Figures_over_all_seasons contains images of plots generated which show plotted data over all the seasons of data 

- Figures_per_season contains images of plots generated which show plotted data over each individual season of data

- Money_puck_data and Standings_hits_PIMS_data contain all the csv file data I used

- python_files contains all the python files I created to analyze/wrange the data, plot the data, and a python file creating a connection to a local SQL server to extract the data

## Up to date Step by Step process of what I have completed

- At first I downloaded CSV data from Money Puck as they had the data I was looking for and understood how the data was formatted within the csv file (All downloaded data was saved in the *money_puck_data* folder)

- I then analyzed how the number of hits and penalty minutes taken has changed over the years. I created the dataframe, obtained the data via the csv files and plotted the data. (These can be found in the (*nhl_hits.py and nhl_penality_taken.py in the python_files folder*))

- Moving forward I wanted to see if there was a relationship between hits, pims and team success. Therefore I intially grouped hits and pims by each team name and created a new csv file for each year with that data. Then I manually entered the standing of the team in that specific year in excel. (This can be found in *Stats_per_team.py* and the data can be found in *Standings_hits_PIMS_data*)

- To analyze the relationship between hits, pims, and team success I plotted graphs (The code can be found in *standing_per_hits_pims.py*)

- I created a local MSSQL server to store all my data which was currently in csv files. I set up the server, created a database and within the database I created a table to store my data. This can be found in (*connection.sql* in the *SQL* folder)

-  Once the SQLserver was set up I started to query my data (found in *queries.sql*), and tested to see if a linear regresson model is appropriate for the data I currently have which can be found in *connection.r* in the *R_files* folder.

## Future analysis I am currently working on and hope to work on 

- Now that I have analyzed the connection between hits, penalty minutes, and the corresponding standing, I will move forward and analyze what are some key attributes of a playoff team. This will specifically focus on what advanced analytics *(corsi, fenwick, expected goals, pdo, etc)* are correleated with team success.

