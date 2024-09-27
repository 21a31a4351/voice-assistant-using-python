from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class YouTube:
    def __init__(self, search_term, headless=False):
        self.search_term = search_term
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        # Use the default executable_path if PATH is set correctly
        service = Service(executable_path='C:/path/to/chromedriver.exe')  # Update this path if not using PATH

        try:
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
        except Exception as e:
            print(f"Failed to initialize WebDriver: {e}")
            raise

    def search_and_play(self):
        try:
            print("Opening YouTube...")
            self.driver.get('https://www.youtube.com')

            print("Waiting for search box...")
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//input[@id="search"]'))
            )
            search_box.clear()
            search_box.send_keys(self.search_term)
            search_box.send_keys(Keys.RETURN)

            print("Waiting for search results...")
            first_video = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//ytd-video-renderer//a[@id="video-title"]'))
            )
            print("Clicking on the first video...")
            first_video.click()

            print("Playing video...")
                        time.sleep(60)  # Adjust the sleep time as necessary

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("Quitting browser...")
            self.driver.quit()

if __name__ == "__main__":
    search_term = "kakli"  # Replace with your desired search term
    try:
        youtube = YouTube(search_term, headless=False)
        youtube.search_and_play()
    except Exception as e:
        print(f"Script failed: {e}")
