# Install the necessary Python packages
pip install selenium
pip install beautifulsoup4
pip install pandas
pip install openpyxl
pip install webdriver_manager

# Create the Python script for web scraping
echo "
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize WebDriver using ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Loop through the first 20 pages of Amazon search results
for page_num in range(1, 21):
    url = f'https://www.amazon.in/s?k=laptop&page={page_num}&crid=1FABNYKSK68DB&qid=1725041073&sprefix=laopt%2Caps%2C267&ref=sr_pg_{page_num}'
    driver.get(url)
    time.sleep(2)  # Wait for the page to fully load

    # Save the HTML content to a file
    with open(f'html_files/page_{page_num}.html', 'w', encoding='utf-8') as file:
        file.write(driver.page_source)

driver.quit()
" > amazon_scraper.py

# Create the Python script for data extraction
echo "
from bs4 import BeautifulSoup
import pandas as pd
import os

# Directory where HTML files are saved
html_dir = 'html_files'

# Lists to store extracted data
names = []
prices = []
links = []

# Loop through each HTML file in the directory
for page_num in range(1, 21):
    file_path = os.path.join(html_dir, f'page_{page_num}.html')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        
        # Find all product elements
        products = soup.find_all('div', {'data-component-type': 's-search-result'})

        for product in products:
            # Extract product details
            name = product.find('span', {'class': 'a-text-normal'})
            price = product.find('span', {'class': 'a-price-whole'})
            link = product.find('a', {'class': 'a-link-normal'})

            if name and price and link:
                names.append(name.get_text(strip=True))
                prices.append(price.get_text(strip=True))
                links.append(f'https://www.amazon.in{link.get('href')}')

# Create a DataFrame and save to Excel
df = pd.DataFrame({
    'Name': names,
    'Price': prices,
    'Link': links
})

df.to_excel('laptop_data.xlsx', index=False)
" > extract_data.py

# Create the directory for HTML files
mkdir html_files












.................................................


....................................................
....................................................


................................................

1. Setup Instructions
Install the necessary Python packages:

selenium: For web browser automation.
beautifulsoup4: For parsing HTML and extracting data.
pandas: For data manipulation and saving to Excel.
openpyxl: For working with Excel files.
webdriver_manager: For automatically managing browser drivers.
sh
Copy code
pip install selenium
pip install beautifulsoup4
pip install pandas
pip install openpyxl
pip install webdriver_manager
Create the necessary Python scripts:

amazon_scraper.py: This script scrapes Amazon search results and saves the HTML content of each page.

extract_data.py: This script extracts data from the saved HTML files and writes it to an Excel file.

Create the directory for HTML files:

html_files: Directory where the HTML files will be stored.
sh
Copy code
mkdir html_files
2. amazon_scraper.py Explanation
python
Copy code
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize WebDriver using ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Loop through the first 20 pages of Amazon search results
for page_num in range(1, 21):
    url = f'https://www.amazon.in/s?k=laptop&page={page_num}&crid=1FABNYKSK68DB&qid=1725041073&sprefix=laopt%2Caps%2C267&ref=sr_pg_{page_num}'
    driver.get(url)
    time.sleep(2)  # Wait for the page to fully load

    # Save the HTML content to a file
    with open(f'html_files/page_{page_num}.html', 'w', encoding='utf-8') as file:
        file.write(driver.page_source)

driver.quit()
webdriver.Chrome(service=Service(ChromeDriverManager().install())): Initializes the WebDriver for Chrome using webdriver_manager to automatically handle the ChromeDriver setup.
driver.get(url): Navigates to the specified URL.
time.sleep(2): Pauses execution for 2 seconds to ensure the page loads completely.
with open(f'html_files/page_{page_num}.html', 'w', encoding='utf-8') as file:: Opens a file to write the HTML content. The file name is dynamically generated based on the page number.
3. extract_data.py Explanation
python
Copy code
from bs4 import BeautifulSoup
import pandas as pd
import os

# Directory where HTML files are saved
html_dir = 'html_files'

# Lists to store extracted data
names = []
prices = []
links = []

# Loop through each HTML file in the directory
for page_num in range(1, 21):
    file_path = os.path.join(html_dir, f'page_{page_num}.html')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        
        # Find all product elements
        products = soup.find_all('div', {'data-component-type': 's-search-result'})

        for product in products:
            # Extract product details
            name = product.find('span', {'class': 'a-text-normal'})
            price = product.find('span', {'class': 'a-price-whole'})
            link = product.find('a', {'class': 'a-link-normal'})

            if name and price and link:
                names.append(name.get_text(strip=True))
                prices.append(price.get_text(strip=True))
                links.append(f'https://www.amazon.in{link.get("href")}')

# Create a DataFrame and save to Excel
df = pd.DataFrame({
    'Name': names,
    'Price': prices,
    'Link': links
})

df.to_excel('laptop_data.xlsx', index=False)
BeautifulSoup(file, 'html.parser'): Parses the HTML file with BeautifulSoup.
soup.find_all('div', {'data-component-type': 's-search-result'}): Finds all div elements with the specified class, indicating individual product entries.
name.get_text(strip=True): Retrieves the text content of the name element, removing any surrounding whitespace.
df.to_excel('laptop_data.xlsx', index=False): Writes the DataFrame to an Excel file named laptop_data.xlsx without including the index column.
4. Notes on Running the Scripts
Running amazon_scraper.py: This script will scrape the data from the specified Amazon pages and save the HTML content to the html_files directory.
Running extract_data.py: This script will read the HTML files, extract product data, and save it to laptop_data.xlsx. Make sure amazon_scraper.py has been run first to populate the html_files directory.
Let me know if you need further clarifications or additional steps!







