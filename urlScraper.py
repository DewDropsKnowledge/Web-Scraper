from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def urlScraper(url, total_urls=100):
    # Initialize a variable to count the scraped URLs
    scraped_urls = 0

    # Set up a headless browser
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    # Open the initial URL
    driver.get(url)

    # Initialize a set to keep track of scraped URLs to avoid duplicates
    scraped_url_set = set()

    with open("article_urls.txt", "a") as file:  # Open the file in append mode
        while True:
            # Scroll down to trigger dynamic loading
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait for a short time to allow new content to load
            time.sleep(2)

            # Find all elements with the class "post-card-inline__header"
            article_header_elements = driver.find_elements(By.CLASS_NAME, "post-card-inline__header")

            for header_element in article_header_elements:
                # Find the <a> element inside the header
                link_element = header_element.find_element(By.TAG_NAME, "a")
                if link_element:
                    # Get the URL from the "href" attribute
                    article_url = link_element.get_attribute("href")

                    # Write the full URL to the file
                    file.write(article_url + "\n")
                    scraped_url_set.add(article_url)
                    scraped_urls += 1

            print(f"Scraped {scraped_urls} URLs")

            # Check if the desired total number of URLs is reached
            if scraped_urls >= total_urls:
                print("Desired total URLs reached.")
                break

            # Check if no more new articles are loaded
            if len(article_header_elements) == 0:
                print("No more pages to scrape.")
                break

    driver.quit()
    print("Scraping complete. A total of", scraped_urls, "URLs have been scraped and saved to 'article_urls.txt'")

