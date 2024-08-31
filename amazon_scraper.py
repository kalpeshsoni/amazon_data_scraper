from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize WebDriver using ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Loop through the first 20 pages of Amazon search results
for page_num in range(1, 21):
    url = f"https://www.amazon.in/s?k=laptop&page={page_num}&crid=1FABNYKSK68DB&qid=1725041073&sprefix=laopt%2Caps%2C267&ref=sr_pg_{page_num}"
    
    driver.get(url)
    time.sleep(2)  # Wait for the page to fully load

    # Save the HTML content to a file
    with open(f"html_files/page_{page_num}.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)

driver.quit()
