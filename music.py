from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class music:
    def __init__(self, search_term):
        self.search_term = search_term
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def open_gaana(self):
        self.driver.get('https://gaana.com/')

    def search_song(self):
        try:
            # Wait for the search box to be visible
            search_box = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'sb'))
            )
            search_box.send_keys(self.search_term)
            search_box.send_keys(Keys.RETURN)
        except Exception as e:
            print(f"Error searching for song: {e}")

    def play_first_song(self):
        try:
            # Wait for the search results to load and click on the first song
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@class="default_thumb rel"]/parent::div/a'))
            ).click()

            # Optional: Handle any pop-ups or consent dialogs
            time.sleep(2)  # Adjust as necessary

            # Wait for the song to start playing (you may adjust the sleep time accordingly)
            time.sleep(10)
        except Exception as e:
            print(f"Error playing song: {e}")

    def close_browser(self):
        self.driver.quit()


# Example usage:
if __name__ == "__main__":
    gaana = music("Shape of You")  # Replace with your desired song
    gaana.open_gaana()
    gaana.search_song()
    gaana.play_first_song()
    time.sleep(30)  # Keep the song playing for 30 seconds
    gaana.close_browser()
