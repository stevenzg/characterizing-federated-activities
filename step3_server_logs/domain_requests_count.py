import csv
from collections import Counter

def count_domain_requests(file_path):
    domain_counter = Counter()

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            domain = row['domain']
            domain_counter[domain] += 1

    return domain_counter

def get_user_and_follower_counts(file_path):
    user_counts = {}
    follower_counts = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            domain = row['domain']
            user_counts[domain] = int(row['user_count'])
            follower_counts[domain] = int(row['followers_count'])
    return user_counts, follower_counts

if __name__ == "__main__":
    input_file_path = "./activitypub_inbox_create.csv"
    output_file_path = "./domain_request_counts.csv"
    user_counts_file_path = "../step2_followed_users_distribution/domain_distribution.csv"
    
    domain_counts = count_domain_requests(input_file_path)
    user_counts, follower_counts = get_user_and_follower_counts(user_counts_file_path)

    with open(output_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['domain', 'count', 'user_count', 'followers_count'])  # Write header
        for domain, count in domain_counts.most_common():
            user_count = user_counts.get(domain, 0)  # Default to 0 if domain not found
            followers_count = follower_counts.get(domain, 0)  # Default to 0 if domain not found
            writer.writerow([domain, count, user_count, followers_count])

    print(f"Domain request counts, user counts, and follower counts have been written to {output_file_path}")
