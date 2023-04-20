# Flipkart-Reviews-Scrapping

This is a Python script that scrapes customer reviews for a product on Flipkart and saves them to a CSV file. The script uses the Requests library to send HTTP requests to the Flipkart website and the BeautifulSoup library to parse the HTML content and extract the reviews and ratings.

The script takes two arguments, start_page and end_page, which specify the range of pages to scrape for reviews. Each page contains up to 10 reviews, so the script can scrape up to 500 reviews (50 pages) for a single product.

The script also excludes the "read more" link from the review text, to ensure that only the complete reviews are saved to the CSV file.

To use the script, you need to provide the URL of the product's review page on Flipkart, which contains the product ID and other parameters. You can modify the script to scrape reviews for any product on Flipkart by changing the URL and the selectors for the review and rating containers.

This script can be useful for anyone who wants to analyze customer feedback for a product on Flipkart, or for data scientists and machine learning practitioners who want to use the reviews as training data for sentiment analysis or other natural language processing tasks.

## Requirements
Python 3.7 or higher 
<br>

Requests library (pip install requests)
<br>

BeautifulSoup library (pip install beautifulsoup4)
<br>

## Usage
1. Clone the repository or download the script file flipkart_reviews_scraper.py.

2. Modify the script to set the url variable to the URL of the product's review page on Flipkart. You can also change the start_page and end_page variables to specify the range of pages to scrape (default is 1-20).

3. Run the script using the command python flipkart_reviews_scraper.py.

4. The script will scrape the reviews and ratings from the specified pages and save them to a CSV file flipkart_reviews.csv in the same directory.
<br>
<br> 

### Disclaimer⚠️⚠️⚠️

***This script is for educational and research purposes only. Use of this script to scrape reviews from Flipkart may be against their Terms of Service. Use at your own risk and responsibility. The creator of this script is not responsible for any legal or ethical issues that may arise from the use of this script.***
