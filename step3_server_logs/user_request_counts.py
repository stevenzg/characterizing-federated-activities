import csv
from collections import Counter

def count_user_requests(file_path):
    user_counter = Counter()
    user_domains = {}

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            username = row['username']
            domain = row['domain']
            user_counter[username] += 1
            user_domains[username] = domain

    return user_counter, user_domains

def get_followers_count(file_path):
    followers_count = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            username = row['username']
            followers = int(row['followers'])
            followers_count[username] = followers
    return followers_count

if __name__ == "__main__":
    input_file_path = "./activitypub_inbox_create.csv"
    output_file_path = "./user_request_counts.csv"
    followers_file_path = "../step2_followed_users_distribution/most_followed_users.csv"
    
    user_counts, user_domains = count_user_requests(input_file_path)
    followers_counts = get_followers_count(followers_file_path)

    with open(output_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['username', 'count', 'domain', 'followers'])  # Write header
        for username, count in user_counts.most_common():
            followers = followers_counts.get(username, 0)  # Default to 0 if username not found
            writer.writerow([username, count, user_domains[username], followers])

    print(f"User request counts and followers have been written to {output_file_path}")
