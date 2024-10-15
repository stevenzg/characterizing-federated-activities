import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def fetch_page_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    users = []
    for user_list in soup.select(".mb-5.relative"):
        account_address_element = user_list.select_one(".text-xs")
        account_address = account_address_element.get_text(strip=True)
        username, domain = account_address.split('@', 1)
        parent = account_address_element.parent
        full_name = parent.select_one(".bg-white").get_text(strip=True)
        followers_element = parent.select_one(".text-4xl")
        followers_text = followers_element.get_text(strip=True)
        followers = re.sub(r'[^\d]', '', followers_text)  # Remove non-digit characters
        users.append((full_name, account_address, username, domain, followers))
    return users

# Fetch data from multiple pages
base_url = "https://most-followed-mastodon-accounts.stefanhayden.com/"
pages = 191  # Maximum number of pages to scrape
all_users = []

for page in range(1, pages + 1):
    url = f"{base_url}?page={page}" if page > 1 else base_url
    all_users.extend(fetch_page_data(url))

# Create a DataFrame
df = pd.DataFrame(all_users, columns=['full_name', 'account_address', 'username', 'domain', 'followers'])

if not df.empty:
    # Save as CSV
    df.to_csv("most_followed_users.csv", index=False)

    print(f"CSV generated successfully with {len(df)} users.")

    # Print the top 10 users for quick review
    print("\nTop 10 Mastodon users:")
    print(df.head(10).to_string(index=False))
else:
    print("No data was extracted. Please check the webpage structure or your internet connection.")
