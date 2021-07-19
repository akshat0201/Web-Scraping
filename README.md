# Web Scraping Project

This project was done on 2 different websites:
 1. Job Website - https://www.timesjobs.com/
 2. Holiday Destination Site - https://www.holidify.com/explore/

 
# Job Website

This project looks for python jobs that were posted recently(the ones marked as 'few days ago') and filters out any skill you might not have.
It puts each of the valid posts into a text file saved by name of company with a link to the application and other skills required. This list refreshes every 5 minutes to keep you up to date.

To run locally, first install the required libraries:
  1. pip install beautifulsoup4
  2. pip install requests

Then run the python file using: python3 scrape.py

# Holiday Destination Site

This project looks through the website and collects the places, the states they're in, ratings, starting prices, famous landmarks and provides a link to book your travel.
This data is stored in a csv file on which all types of data analysis can be done.

To run locally, first install the required libraries:
  1. pip install beautifulsoup4
  2. pip install requests
  3. pip install pandas
  4. pip install numpy

Then open the holiday.ipynb file in Jupyter Notebook and run.
