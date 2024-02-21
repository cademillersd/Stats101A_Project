Stats 101A Project - Miller, Gervase, Sundar

We are measuring the sentiment of the FOMC mintues vs. the percent change in S&P 500 index value from the week before minutes are released to the week after.

Roughly, our process went as follows:
1) Compiled a list of 112 FOMC minutes documents from the FOMC website. This list spans from January 2010 to December 2023
2) Ran an economic, lexicon-based sentiment analysis in Python. Exported the results into a CSV file. 
3) Compiled a list of the 112 FOMC minutes release dates. Calculated the average S&P 500 index price for the week prior and the week following the release dates.
4) Calculated the percentage change between the week prior and the week following for all 112 FOMC minutes.
5) Created a linear model that compares the sentiment scores of the minutes vs. the percentage change of the S&P 500 index price. 
6) Analyzed and interpreted results. (This is still up in the air and the majority of the work)
