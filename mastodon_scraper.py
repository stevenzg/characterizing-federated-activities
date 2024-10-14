import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_page_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    users = []
    for user_list in soup.select(".mb-5.relative"):
        for user in user_list.select(".text-xs"):
            user_data = user.get_text(strip=True, separator='\n')
            users.append(user_data)
    return users

# Fetch data from multiple pages
base_url = "https://most-followed-mastodon-accounts.stefanhayden.com/"
pages = 191  # Maximum number of pages to scrape
all_users = []

for page in range(1, pages + 1):
    url = f"{base_url}?page={page}" if page > 1 else base_url
    all_users.extend(fetch_page_data(url))
    if len(all_users) >= 7500:
        all_users = all_users[:7500]
        break

# Create a DataFrame
df = pd.DataFrame(all_users, columns=['account_address'])

if not df.empty:
    # Add 'Show boosts' and 'Notify on new posts' columns
    df['Show boosts'] = 'TRUE'
    df['Notify on new posts'] = 'TRUE'

    # Save as CSV
    df.to_csv("mastodon_top_users_7500.csv", index=False)

    print(f"CSV generated successfully with {len(df)} users.")

    # Print the top 10 users for quick review
    print("\nTop 10 Mastodon users:")
    print(df.head(10).to_string(index=False))
else:
    print("No data was extracted. Please check the webpage structure or your internet connection.")
