import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h2')  # Example: find all <h2> elements
        return [title.text.strip() for title in titles]
    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    url = "https://blog.scrapinghub.com"  # Example site
    headlines = scrape_titles(url)
    print("📰 Scraped Headlines:")
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")