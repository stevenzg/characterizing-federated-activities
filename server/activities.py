import csv
import re
from collections import defaultdict

def analyze_log_file(log_file_path):
    request_types = defaultdict(int)
    
    with open(log_file_path, 'r') as file:
        for line in file:
            match = re.search(r'method=(\w+) path=([^\s]+).*controller=([^\s]+) action=([^\s]+)', line)
            if match:
                method, path, controller, action = match.groups()
                key = (method, path, controller, action)
                request_types[key] += 1

    return request_types

def write_to_csv(request_types, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['method', 'path', 'controller', 'action', 'count'])
        
        for (method, path, controller, action), count in request_types.items():
            writer.writerow([method, path, controller, action, count])

def main():
    log_file_path = '../logs/mastodon-web.log'
    output_file = 'request_types.csv'
    
    request_types = analyze_log_file(log_file_path)
    write_to_csv(request_types, output_file)
    
    print(f"Analysis complete. Results written to {output_file}")

if __name__ == "__main__":
    main()
