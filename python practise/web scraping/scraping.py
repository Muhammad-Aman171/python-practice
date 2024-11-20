

# import requests
# from bs4 import BeautifulSoup
# import json

# def scrape_website(url):
#     try:
#         # Website ki HTML content download karna
#         response = requests.get(url)
#         response.raise_for_status()
#         html_content = response.text
        
#         # HTML parsing
#         soup = BeautifulSoup(html_content, 'html.parser')
        
#         # Website ki maloomat ko extract karna
#         data = {
#             "title": soup.title.string if soup.title else "No Title Found",
#             "headings": [heading.get_text(strip=True) for heading in soup.find_all(['h1', 'h2', 'h3'])],
#             "paragraphs": [para.get_text(strip=True) for para in soup.find_all('p')],
#             "links": [link.get('href') for link in soup.find_all('a', href=True)]
#         }
        
#         # JSON file mein maloomat store karna
#         with open("website_data.json", "w", encoding="utf-8") as json_file:
#             json.dump(data, json_file, ensure_ascii=False, indent=4)
        
#         print("Scraping complete! Data saved in 'website_data.json'.")
    
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching the website: {e}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # URL input
# website_url = input("Enter the website URL: ").strip()
# scrape_website(website_url)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import time

def scrape_dynamic_website(url):
    try:
        # Selenium browser setup
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run browser in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = Service("chromedriver")  # Make sure you have ChromeDriver installed and in PATH
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Open the website
        # driver.get(url)
        time.sleep(5)  # Wait for JavaScript to load content

        # Extract data
        data = {
            "title": driver.title,
            "headings": [element.text for element in driver.find_elements(By.TAG_NAME, 'h1')] +
                        [element.text for element in driver.find_elements(By.TAG_NAME, 'h2')] +
                        [element.text for element in driver.find_elements(By.TAG_NAME, 'h3')],
            "paragraphs": [element.text for element in driver.find_elements(By.TAG_NAME, 'p')],
            "links": [element.get_attribute('href') for element in driver.find_elements(By.TAG_NAME, 'a') if element.get_attribute('href')],
        }

        # Save to JSON file
        with open("dynamic_website_data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        print("Scraping complete! Data saved in 'dynamic_website_data.json'.")

        # Close the browser
        driver.quit()

    except Exception as e:
        print(f"An error occurred: {e}")

# Input the website URL
website_url = input("Enter the website URL: ").strip()
scrape_dynamic_website(website_url)

