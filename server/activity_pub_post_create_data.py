import csv

def count_rows(csv_file_path):
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        row_count = sum(1 for row in csv_reader) - 1  # Subtract 1 to exclude the header row
    return row_count

csv_file_path = 'activitypub_post_create.csv'
total_rows = count_rows(csv_file_path)
print(f"The file '{csv_file_path}' contains {total_rows} rows of data.")
