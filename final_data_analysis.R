## Gather sentiment scores
sentiment_data <- as.data.frame(read.csv("C:/Users/cadem/OneDrive/Documents/FOMC_minutes_sentiment_scores.csv", header = FALSE))
sentiment_scores <- sentiment_data[, 2]
sentiment_scores <- sentiment_data[c(-93, -94), ]
sentiment_scores

## Gather percentage changes
sp_percent_change_data <- as.data.frame(read.csv("C:/Users/cadem/OneDrive/Documents/filename"))
percentage_change_data <- sp_percent_change_data[, 3]
percentage_change_data <- percentage_change_data[c(-93, -94, ]
percentage_change_data

## Put the data into one data frame
final_data <- data.frame("Sentiment Scores" = sentiment_scores, "Market Percentage Change" = percentage_change_data)
final_data

## Data analysis
model <- lm(percentage_change_data ~ sentiment_scores, data = final_data)
summary(model)
