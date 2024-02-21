library(dplyr)
library(stringr)
library(readr)


release <- read.csv("minutesnumeric.csv", header = FALSE)
sp500 <- read.csv("dailysp.csv")

release_dates <- release[[2]]
release_dates <- release_dates[-93]
data_for_release_dates <- filter(sp500, Date %in% release_dates)



weeks_prior <- c()
weeks_after <- c()
avg_price_week_prior <- c()
avg_price_week_after <- c()

for(i in 1:109) {
  weeks_prior[i] <- as.character(as.Date(data_for_release_dates[i, 1]) - 7) ## find date for 1 week before minutres release date
}

for(j in 1:109) {
  weeks_after[j] <- as.character(as.Date(data_for_release_dates[j, 1]) + 7) ## find date for 1 week after minutres release date
}


data_for_week_prior <- filter(sp500, Date %in% weeks_prior)
data_for_week_after <- filter(sp500, Date %in% weeks_after)


dates <- data.frame(release_dates, weeks_prior, weeks_after)


prior_join <- left_join(data_for_week_prior, dates, by = c("Date"= "weeks_prior"))
after_join <- inner_join(prior_join, data_for_week_after, by = c("weeks_after" = "Date"))
final_table <- inner_join(final_table, data_for_release_dates, by = c("release_dates" = "Date"))



with_mutate1 <- final_table %>%
  mutate(avg_price_week_prior = (Open.x + Open)/2) %>%
  mutate(avg_price_week_after = (Open + Open.y)/2) %>%
  mutate(percent_change = avg_price_week_after/avg_price_week_prior)


sp_data1 <- data.frame(release_date = with_mutate$release_dates, 
                      avg_price_week_prior = with_mutate$avg_price_week_prior,
                      avg_price_week_after = with_mutate$avg_price_week_after,
                      percent_change = with_mutate$percent_change
                      )

before_date_after1 <- data.frame(weeks_prior, release_dates, weeks_after)

write.csv(with_mutate1, "price_table1.csv", row.names = FALSE)
write.csv(sp_data1, "sp_data1.csv", row.names = FALSE)
write.csv(before_date_after1, "before_date_after.csv", row.names = FALSE)



anti_join(release, final_table, by = c("V2" = "release_dates"))





scores <- read.csv("FOMC_minutes_sentiment_scores.csv")
head(scores)

scores[,2]
