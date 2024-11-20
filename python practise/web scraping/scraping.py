

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



