# google_search_scraper.py

from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from googlesearch import search
import time
import random

class GoogleSearchScraper:
    @staticmethod
    def check_and_remove_social_media(url):
        parsed_url = urlparse(url)
        if parsed_url.netloc.endswith('facebook.com') or \
                parsed_url.netloc.endswith('youtube.com') or \
                parsed_url.netloc.endswith('linkedin.com') or \
                parsed_url.netloc.endswith('twitter.com'):
            return False
        else:
            return True

    @staticmethod



    def search_links(query, max_results=4, retry_attempts=3):
        try:
            urls = []
            count = 0
            for _ in range(retry_attempts):
                try:
                    for j in search(query):
                        urls.append(j)
                        count += 1
                        if count >= max_results:
                            return urls
                        time.sleep(2)  # Custom delay of 2 seconds between requests
                except Exception as e:
                    print("Error occurred while searching:", e)
                    if "429" in str(e):  # Check if the error is due to rate limiting
                        print("Rate limit exceeded. Retrying after a delay.")
                        time.sleep(60 * (2 ** _) + random.random() * 10)  # Exponential backoff with jitter
                    else:
                        return []
            print("Max retry attempts reached. Exiting.")
            return []
        except Exception as e:
            print("Error occurred:", e)
            return []

    @staticmethod
    def scrape_p_tags(urls):
        all_text = ""
        for url in urls:
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                p_tags = soup.find_all('p')
                for p_tag in p_tags:
                    all_text += p_tag.get_text() + "\n"
            except Exception as e:
                print(f"Error scraping {url}: {e}")
        return all_text

    @staticmethod
    def google_search(query):
        urls = GoogleSearchScraper.search_links(query)
        combined_text = GoogleSearchScraper.scrape_p_tags(urls)
        return combined_text
