CREATE DATABASE NHLTrends;

USE NHLtrends;
GO

CREATE TABLE year_hits_pims_standing(
    year VARCHAR(10),
    team VARCHAR(10),
    hitsfor INT,
    pimsfor INT,
    standing INT
);


