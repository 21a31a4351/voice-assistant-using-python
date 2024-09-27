import requests
import pyttsx3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
class NewsAPIReader:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://newsapi.org/v2/top-headlines'
    def head(self, country='in', category=None):
        params = {
            'country': country,
            'apiKey': self.api_key
        }
        if category:
            params['category'] = category


        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if data.get('status') == 'ok':
            articles = data.get('articles', [])
            headlines = []
            for idx, article in enumerate(articles, start=1):
                    headline = f"{article['title']} from {article['source']['name']}."
                    headlines.append(headline)
            return headlines
        else:
                print(f"Failed to fetch news: {data.get('message')}")
                return []
    def display_headlines_in_browser(self, headlines):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Create an HTML template to display headlines
        html_content = "<html><head><title>News Headlines</title></head><body><h1>Top Headlines</h1><ul>"
        for headline in headlines:
            html_content += f"<li>{headline}</li>"
        html_content += "</ul></body></html>"

        # Open a blank page and inject the HTML content
        driver.get("data:text/html," + html_content)

        # Keep the browser open until the user closes it
        input("Press Enter to close the browser...")

        # Close the browser
        driver.quit()


def read_out_headlines(headlines):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 130)
    engine.setProperty('voice', voices[1].id)

    for headline in headlines:
        engine.say(headline)
        engine.runAndWait()

#
# if __name__ == "__main__":
#     api_key = ss.key
#
#     news_reader = NewsAPIReader(api_key)
#     headlines = news_reader.head()
#
#     if headlines:
#         read_out_headlines(headlines)
#         news_reader.display_headlines_in_browser(headlines)
#     else:
#         print("No headlines to display.")
