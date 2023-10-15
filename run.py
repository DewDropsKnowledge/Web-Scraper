from urlScraper import urlScraper
from scrapeArticlesFromUrls import scrapeArticlesFromUrl
from articleScraper import articleScraper
import time

print('Article Scraper')
url = input("Please input URL with article directory: ")
quantity_url = input("Please input total amount of URLs wanted: ")

# Use the urlScraper function to scrape article URLs and save them to a file
urlScraper(url, quantity_url)

# Use the scrapeArticlesFromUrls function to scrape articles from the saved URLs
scrapeArticlesFromUrl()

time.sleep(6000)
