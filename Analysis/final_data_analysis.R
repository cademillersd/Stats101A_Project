## Gather sentiment scores
sentiment_data <- as.data.frame(read.csv("C:/Users/cadem/OneDrive/Documents/FOMC_minutes_sentiment_scores.csv", header = FALSE))
sentiment_scores <- sentiment_data[, 2]

## Gather percentage changes
sp_percent_change_data <- as.data.frame(read.csv("C:/Users/cadem/OneDrive/Documents/transformed_market_data.csv"))
percentage_change_data <- sp_percent_change_data[, 1]
percentage_change_data <- c(0.00, percentage_change_data)
percentage_change_data

## Put the data into one data frame
final_data <- data.frame("Sentiment Scores" = sentiment_scores, "Futures Peracentage Change" = percentage_change_data)
final_data

## Data analysis
linear_model <- lm(percentage_change_data ~ sentiment_scores, data = final_data)
plot((percentage_change_data) ~ (sentiment_scores), data = final_data, col = "purple", pch = 16)
abline(linear_model, col = "blue")

summary(linear_model)
plot(linear_model)
