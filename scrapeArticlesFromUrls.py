from articleScraper import articleScraper

def scrapeArticlesFromUrl():
    # Load the list of article URLs from the file
    with open("article_urls.txt", "r") as file:
        article_urls = file.read().splitlines()

    # Loop through each URL and scrape the article
    for url in article_urls:
        articleScraper(url)
