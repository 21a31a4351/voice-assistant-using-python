from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class WikipediaSearcher:
    def __init__(self, search_term):
        self.search_term = search_term
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def search(self):
        try:
            # Open Wikipedia
            self.driver.maximize_window()
            self.driver.get("https://www.wikipedia.org/")

            # Find the search input field
            search_input = self.driver.find_element(By.NAME, "search")

            # Enter the search term
            search_input.send_keys(self.search_term)

            # Press ENTER to start the search
            search_input.send_keys(Keys.RETURN)

            # Wait for a few seconds to let the search results load
            time.sleep(30)

            # Print the title of the page
            print(self.driver.title)
        finally:
            # Close the WebDriver
            self.driver.quit()


