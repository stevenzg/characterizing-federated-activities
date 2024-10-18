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

if __name__ == "__main__":
    input_file_path = "./activitypub_inbox_create.csv"
    output_file_path = "./domain_request_counts.csv"
    domain_counts = count_domain_requests(input_file_path)

    with open(output_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['domain', 'count'])  # Write header
        for domain, count in domain_counts.most_common():
            writer.writerow([domain, count])

    print(f"Domain request counts have been written to {output_file_path}")
