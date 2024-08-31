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
    file_path = os.path.join(html_dir, f"page_{page_num}.html")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        
        # Find all product elements (updated the selector based on actual HTML structure)
        products = soup.find_all('div', {'data-component-type': 's-search-result'})

        for product in products:
            # Extract product details (update the selectors based on actual HTML structure)
            name = product.find('span', {'class': 'a-text-normal'})
            price = product.find('span', {'class': 'a-price-whole'})
            link = product.find('a', {'class': 'a-link-normal'})

            if name and price and link:
                names.append(name.get_text(strip=True))
                prices.append(price.get_text(strip=True))
                links.append(f"https://www.amazon.in{link.get('href')}")

# Create a DataFrame and save to Excel
df = pd.DataFrame({
    'Name': names,
    'Price': prices,
    'Link': links
})

df.to_excel('laptop_data.xlsx', index=False)
