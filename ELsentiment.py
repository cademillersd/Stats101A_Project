import csv
import PyPDF2

## Loads and defines the lexicon
def load_lexicon(lexicon_filename):
    lexicon = {}
    with open(lexicon_filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            token, sentiment, polarity = row
            lexicon[token] = {'sentiment': float(sentiment), 'polarity': int(polarity)}
    return lexicon

## Converts the minutes from a pdf to parsable text
def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

## Conducts the sentiment analysis and returns a final sentiment score
def analyze_sentiment(text, lexicon):
    tokens = text.lower().split()  # Tokenize text
    total_score = 0
    present_token = 0
    for token in tokens:
        if token in lexicon:
            sentiment = lexicon[token]['sentiment']
            present_token += 1
            total_score += sentiment
    sentiment_score = total_score / present_token ## This standardizes the total scores
    return sentiment_score  

if __name__ == '__main__':
    ## Initializes variables
    month_and_year = ["January2010", "March2010", "April2010", "June2010", "August2010",
                      "September2010", "November2010", "December2010", "January2011", 
                      "March2011", "April2011", "June2011", "August2011", "September2011",
                      'November2011', "December2011", "January2012", "March2012", 
                      "April2012", "June2012", "August2012", "September2012", "October2012",
                      "December2012", "January2013", "March2013", "April2013", "June2013",
                      "July2013", "September2013", "October2013", "December2013",
                      "January2014", "March2014", "April2014", "June2014", "July2014",
                      "September2014", "October2014", "December2014", "January2015",
                      "March2015", "April2015", "June2015", "July2015", "September2015",
                      "October2015", "December2015", "January2016", "March2016", "April2016",
                      "June2016", "July2016", "September2016", "November2016", "December2016",
                      "January2017", "March2017", "May2017", "June2017", "July2017",
                      "September2017", "October2017", "December2017", "January2018",
                      "March2018", "May2018", "June2018", "July2018", "September2018",
                      "November2018", "December2018", "January2019", "March2019", "April2019",
                      "June2019", "July2019", "September2019", "October2019", "December2019",
                      "January2020", "March2020", "April2020", "June2020", "July2020",
                      "September2020", "November2020", "December2020", "January2021", 
                      "March2021", "April2021", "June2021", "July2021", "September2021", 
                      "November2021", "December2021", "January2022", "March2022", "May2022",
                      "June2022", "July2022", "September2022", "November2022", "December2022",
                      "January2023", "March2023", "May2023", "June2023", "July2023", 
                      "September2023", "October2023", "December2023"]
    release_date = ["Feb 17, 2010", 
                    "Apr 6, 2010",
                    "May 19, 2010",
                    "July 14, 2010",
                    "Aug 31, 2010",
                    "Oct 12, 2010",
                    "Nov 23, 2010",
                    "Jan 4, 2011",
                    "February 16, 2011",
                    "April 05, 2011",
                    "May 18, 2011",
                    "July 12, 2011",
                    "August 30, 2011",
                    "October 12, 2011",
                    "November 22, 2011",
                    "January 03, 2012",
                    "February 15, 2012",
                    "April 03, 2012",
                    "May 16, 2012",
                    "July 11, 2012",
                    "August 22, 2012",
                    "October 04, 2012",
                    "November 14, 2012",
                    "January 03, 2013",
                    "February 20, 2013",
                    "April 10, 2013",
                    "May 22, 2013",
                    "July 10, 2013",
                    "August 21, 2013",
                    "October 09, 2013",
                    "November 20, 2013",
                    "January 08, 2014",
                    "February 19, 2014",
                    "April 09, 2014",
                    "May 21, 2014",
                    "July 09, 2014",
                    "August 20, 2014",
                    "October 08, 2014",
                    "November 19, 2014",
                    "January 07, 2015",
                    "February 18, 2015",
                    "April 08, 2015",
                    "May 20, 2015",
                    "July 08, 2015",
                    "August 19, 2015",
                    "October 08, 2015",
                    "November 18, 2015",
                    "January 06, 2016",
                    "February 17, 2016",
                    "April 06, 2016",
                    "May 18, 2016",
                    "July 06, 2016",
                    "August 17, 2016",
                    "October 12, 2016",
                    "November 23, 2016",
                    "January 04, 2017",
                    "February 22, 2017",
                    "April 05, 2017",
                    "May 24, 2017",
                    "July 05, 2017",
                    "August 16, 2017",
                    "October 11, 2017",
                    "November 22, 2017",
                    "January 03, 2018",
                    "February 21, 2018",
                    "April 11, 2018",
                    "May 23, 2018",
                    "July 05, 2018",
                    "August 22, 2018",
                    "October 17, 2018",
                    "November 29, 2018",
                    "January 09, 2019",
                    "February 20, 2019",
                    "April 10, 2019",
                    "May 22, 2019",
                    "July 10, 2019",
                    "August 21, 2019",
                    "October 09, 2019",
                    "November 20, 2019",
                    "January 03, 2020",
                    "February 19, 2020",
                    "April 08, 2020",
                    "May 20, 2020",
                    "July 01, 2020",
                    "August 19, 2020",
                    "October 07, 2020",
                    "November 25, 2020",
                    "January 06, 2021",
                    "February 17, 2021",
                    "April 7, 2021",
                    "May 19, 2021",
                    "July 7, 2021",
                    "August 18, 2021",
                    "October 13, 2021",
                    "November 24, 2021",
                    "January 05, 2022",
                    "February 16, 2022",
                    "April 06, 2022",
                    "May 25, 2022",
                    "July 06, 2022",
                    "August 17, 2022",
                    "October 12, 2022",
                    "November 23, 2022",
                    "January 04, 2023",
                    "February 22, 2023",
                    "April 12, 2023",
                    "May 24, 2023",
                    "July 05, 2023",
                    "August 16, 2023",
                    "October 11, 2023",
                    "November 21, 2023",
                    "January 03, 2024"]
    sentiment_file = "C:/Users/cadem/OneDrive/Documents/FOMC_minutes_sentiment_scores.csv"
    counter = 0 ## Used to keep track of month_and_year index for parallel indexing
    
    ## Creates csv file for sentiment scores
    ## Every time the code is run this will completely overwrite the old file with new data
    with open(sentiment_file, 'w') as file:
        pass
    
    ## Runs all the functions
    lexicon = load_lexicon('C:/Users/cadem/Downloads/Economic_Lexicon.csv')  
    for date in month_and_year:
        pdf_minutes = "C:/Users/cadem/OneDrive/Documents/FOMC Minutes 2010-2023/{}.pdf".format(date)
        pdf_text = extract_text_from_pdf(pdf_minutes)
        sentiment_score = analyze_sentiment(pdf_text, lexicon)
        sentiment_data = [[date, sentiment_score, release_date[counter]]]
        counter += 1

        with open(sentiment_file, 'a', newline="") as scores:
            writer = csv.writer(scores)
            writer.writerows(sentiment_data)
     
        print("Sentiment score for {}:".format(date), sentiment_score)