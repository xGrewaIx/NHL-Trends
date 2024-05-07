library(RODBC)
library(dplyr)
library(DBI)
library(ggplot2)

# Connect to local SQL server
conn <- odbcDriverConnect("driver={SQL Server};server=(local);
    database=NHLTrends;trusted_connection=yes")

# Query all data and put it all into a dataframe for modelling
query <- sqlQuery(conn,"SELECT * FROM year_hits_pims_standing")
df <- as.data.frame(query)
head(df)

# Plot hits vs standings
ggplot(df, aes(x=standing, y=hitsfor)) + 
    geom_point() + 
    geom_smooth(method="lm", se=FALSE) +
    ggtitle("Hits vs Standing")

# Plot penalty minutes vs standings
ggplot(df, aes(x=standing, y=pimsfor)) + 
    geom_point() + 
    geom_smooth(method="lm", se=FALSE) +
    ggtitle("Penalty Minutes vs Standing")


## Initially we can see that there probably is very low correlation
## Between standing and hits/pims

# Model with hits and penalty minutes as predictors
model <- lm(standing ~ hitsfor + pimsfor, data=df)
summary(model)
# Plot diagnostics to check to see if linear regression is appropriate
hist(model$residuals)
qqnorm(model$residuals)
qqline(model$residuals)
plot(model$fitted.values, model$residuals)
# From the diagnostics we see that it the conditions for 
# Linear regression are not satisfied therefore we do not continue


## Can try transformations