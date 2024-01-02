# NHL-Trends

## Information about what this repository

This repository showcases my ongoing work in the analysis of how ice hockey has evolved since the cap era (2005-06). Later on I will dive into each Stanley Cup winning team and try to find common attributes amongst Stanley Cup winning teams

*Data from the lockout (2012-2013) and the Covid Seasons (2019-2020 and 2020-21)were not used due to the inconsistency in games played as a full 82 game regular season was not completed during these years*

**Data was obtained from Money Puck (https://moneypuck.com/teams.htm)**

## What each folder contains

- Figures_over_all_seasons contains images of plots generated which show plotted data over all the seasons of data 

- Figures_per_season contains images of plots generated which show plotted data over each individual season of data

- Money_puck_data and Standings_hits_PIMS_data contain all the csv file data I used

- python_files contains all the python files I created to analyze the data and plot the data

## Up to date Step by Step process of what I have completed

- At first I downloaded CSV data from Money Puck as they had the data I was looking for and understood how the data was formatted within the csv file (All downloaded data was saved in the *money_puck_data* folder)

- I then analyzed how the number of hits and penalty minutes taken has changed over the years. I created the dataframe, obtained the data via the csv files and plotted the data. (These can be found in the (*nhl_hits.py and nhl_penality_taken.py in the python_files folder*))

- Moving forward I wanted to see if there was a relationship between hits, pims and team success. Therefore I intially grouped hits and pims by each team name and created a new csv file for each year with that data. Then I manually entered the standing of the team in that specific year in excel. (This can be found in *Stats_per_team.py and the data can be found in Standings_hits_PIMS_data*)

- To analyze the relationship between hits, pims, and team success I plotted graphs (The code can be found in *standing_per_hits_pims.py*)

## Future analysis I am currently working on and hope to work on 

- Next I want to analyze how much scoring has changed over the years as there has been a spike in goals scored in recent years and a dip in goaltending performance

- Something I would love to analyze in the future is how important elite goaltending is for team success. (Is a elite goaltender neccessary for winning a Stanley cup)

