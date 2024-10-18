import csv
import re
from datetime import datetime

def analyze_log_file(log_file_path):
    log_data = []
    
    with open(log_file_path, 'r') as file:
        for line in file:
            match = re.search(r'(\w+ \d+ \d+:\d+:\d+).*method=POST.*controller=ActivityPub::InboxesController action=create status=(\d+) allocations=(\d+) duration=([\d.]+) view=([\d.]+) db=([\d.]+) key=([^\s]+)', line)
            if match:
                time, status, allocations, duration, view, db, key = match.groups()
                domain_match = re.search(r'https://([^/]+)/users/([^#]+)', key)
                if domain_match:
                    domain, username = domain_match.groups()
                    log_data.append({
                        'time': time,
                        'status': status,
                        'allocations': allocations,
                        'duration': duration,
                        'view': view,
                        'db': db,
                        'key': key,
                        'domain': domain,
                        'username': username
                    })
    return log_data

def write_to_csv(log_data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['time', 'status', 'allocations', 'duration', 'view', 'db', 'key', 'domain', 'username']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in log_data:
            writer.writerow(row)

def main():
    log_file_path = '../logs/mastodon-web.log'
    output_file = 'activitypub_inbox_create.csv'
    
    log_data = analyze_log_file(log_file_path)
    write_to_csv(log_data, output_file)
    
    print(f"Analysis complete. Results written to {output_file}")

if __name__ == "__main__":
    main()
