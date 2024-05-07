-- Get average hits for each year
SELECT AVG(hitsfor) AS average_hits, year
FROM [NHLTrends].[dbo].[year_hits_pims_standing]
GROUP BY year;

-- Get average pims per year
SELECT AVG(pimsfor) as average_pims, year
FROM [NHLTrends].[dbo].[year_hits_pims_standing]
GROUP BY year;



-- Querying to find what teams had above average hits, pims and what their standing was
SELECT t.team, t.year, t.hitsfor, t.pimsfor, t.standing
FROM [NHLTrends].[dbo].[year_hits_pims_standing] AS t
WHERE t.hitsfor > 
    (
        SELECT AVG(sub.hitsfor)
        FROM [NHLTrends].[dbo].[year_hits_pims_standing] AS sub 
        WHERE sub.year = t.year
    )
    AND t.pimsfor > 
    (
        SELECT AVG(sub.pimsfor)
        FROM [NHLTrends].[dbo].[year_hits_pims_standing] AS sub 
        WHERE sub.year = t.[year]
    )
ORDER BY t.hitsfor, t.pimsfor;
-- We see that there are 102 teams that had above average hits AND pims


SELECT t.team, t.year, t.hitsfor, t.pimsfor, t.standing
FROM [NHLTrends].[dbo].[year_hits_pims_standing] AS t
-- for some reason when I do > 16 it gives results for all
-- teams with standing < 16 and < 16 does opposite
-- so used  16
WHERE t.[standing] < 16
    AND t.hitsfor > 
    (
        SELECT AVG(sub.hitsfor)
        FROM [NHLTrends].[dbo].[year_hits_pims_standing] AS sub 
        WHERE sub.year = t.year
    )
    AND t.pimsfor > 
    (
        SELECT AVG(sub.pimsfor)
        FROM [NHLTrends].[dbo].[year_hits_pims_standing] AS sub 
        WHERE sub.year = t.[year]
    )
ORDER BY t.hitsfor, t.pimsfor, t.standing;
-- From this query we find only 48 teams made the top 16 in the league
-- when they had above average hits and pims
    
-- Find out how many teams per season had above average hits/pims
SELECT COUNT(t.team) AS number_of_teams, t.[year], AVG(t.hitsfor) AS avg_hits_for, AVG(t.pimsfor) AS avg_pims_for
FROM [NHLTrends].[dbo].[year_hits_pims_standing] AS t
    WHERE t.hitsfor > 
    (
        SELECT AVG(sub.hitsfor)
        FROM [NHLTrends].[dbo].[year_hits_pims_standing] AS sub 
        WHERE sub.year = t.year
    )
    AND t.pimsfor > 
    (
        SELECT AVG(sub.pimsfor)
        FROM [NHLTrends].[dbo].[year_hits_pims_standing] AS sub 
        WHERE sub.year = t.[year]
    )
GROUP BY t.[year]
ORDER BY number_of_teams DESC;

-- Find out how many top 16 teams per season had above average hits/pims
SELECT COUNT(t.team) AS number_of_teams, t.[year], AVG(t.hitsfor) AS avg_hits_for, AVG(t.pimsfor) AS avg_pims_for
FROM [NHLTrends].[dbo].[year_hits_pims_standing] AS t
WHERE t.standing < 16    
    AND t.hitsfor > 
    (
        SELECT AVG(sub.hitsfor)
        FROM [NHLTrends].[dbo].[year_hits_pims_standing] AS sub 
        WHERE sub.year = t.year
    )
    AND t.pimsfor > 
    (
        SELECT AVG(sub.pimsfor)
        FROM [NHLTrends].[dbo].[year_hits_pims_standing] AS sub 
        WHERE sub.year = t.[year]
    )
GROUP BY t.[year]
ORDER BY number_of_teams DESC;

-- From the above we basically see that having a high amount of hits
-- and a high amount of pims did not lead to  a top 16 team
-- now I will check hits and pims individually

-- Find out how many top 16 teams per season had above average hits
SELECT COUNT(t.team) AS number_of_teams, t.[year], AVG(t.hitsfor) AS avg_hits_for
FROM [NHLTrends].[dbo].[year_hits_pims_standing] AS t
WHERE t.standing < 16
    AND t.hitsfor > 
    (
        SELECT AVG(sub.hitsfor)
        FROM [NHLTrends].[dbo].[year_hits_pims_standing] AS sub 
        WHERE sub.year = t.year
    )
GROUP BY t.[year]
ORDER BY number_of_teams DESC;

-- Find out how many top 16 teams per season had above average pims
SELECT COUNT(t.team) AS number_of_teams, t.[year], AVG(t.pimsfor) AS avg_pims_for
FROM [NHLTrends].[dbo].[year_hits_pims_standing] AS t
WHERE t.standing < 16    
    AND t.pimsfor > 
    (
        SELECT AVG(sub.pimsfor)
        FROM [NHLTrends].[dbo].[year_hits_pims_standing] AS sub 
        WHERE sub.year = t.[year]
    )
GROUP BY t.[year]
ORDER BY number_of_teams DESC;