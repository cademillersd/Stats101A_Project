Stats 101A Project - Miller, Gervase, Sundar

We are measuring the sentiment of the Federal Open Market Committee (FOMC) mintues vs. the percent change in S&P 500 index value from the week before minutes are released to the week after.

Roughly, our process went as follows:
1) Compiled a list of 112 FOMC minutes documents from the FOMC website; compiled a list of the 112 FOMC minutes release dates. This list spans from January 2010 to December 2023.
2) Ran an economic, lexicon-based sentiment analysis. Exported the results into a CSV file. 
3) Calculated the average S&P 500 index opening price for the weeks prior and the weeks following the release dates. Seven (7) release dates have market closures within plus or minus a week. These respective FOMC minutes were removed from our data to maintain statistical integrity.
4) Calculated the percentage change between the week prior and the week following for all 105 FOMC minutes.
5) Created a linear model that compares the sentiment scores of the minutes vs. the percentage change of the S&P 500 index price. 
6) Analyzed and interpreted results. See presentation: (insert slides link here)
