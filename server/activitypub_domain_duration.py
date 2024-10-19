import csv
from collections import defaultdict
import statistics

def analyze_domain_durations(input_file, output_file):
    domain_durations = defaultdict(list)
    
    # Read the input CSV file and collect durations for each domain
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            domain = row['domain']
            duration = float(row['duration'])
            domain_durations[domain].append(duration)
    
    # Calculate statistics for each domain
    domain_stats = []
    for domain, durations in domain_durations.items():
        stats = {
            'domain': domain,
            'avg_duration': statistics.mean(durations),
            'median_duration': statistics.median(durations),
            'max_duration': max(durations),
            'min_duration': min(durations)
        }
        domain_stats.append(stats)
    
    # Write the results to the output CSV file
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['domain', 'avg_duration', 'median_duration', 'max_duration', 'min_duration']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for stats in domain_stats:
            writer.writerow(stats)

def main():
    input_file = 'activitypub_inbox_create.csv'
    output_file = 'activitypub_domain_duration.csv'
    
    analyze_domain_durations(input_file, output_file)
    print(f"Analysis complete. Results written to {output_file}")

if __name__ == "__main__":
    main()
