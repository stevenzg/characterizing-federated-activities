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

if __name__ == "__main__":
    input_file_path = "./activitypub_inbox_create.csv"
    output_file_path = "./user_request_counts.csv"
    user_counts, user_domains = count_user_requests(input_file_path)

    with open(output_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['username', 'count', 'domain'])  # Write header
        for username, count in user_counts.most_common():
            writer.writerow([username, count, user_domains[username]])

    print(f"User request counts have been written to {output_file_path}")
