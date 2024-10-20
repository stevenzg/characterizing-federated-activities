import re

def filter_log_file(input_log_path, output_log_path):
    pattern = r'method=POST path=/users/Steven/inbox.*controller=ActivityPub::InboxesController action=create'
    
    with open(input_log_path, 'r') as input_file, open(output_log_path, 'w') as output_file:
        for line in input_file:
            if re.search(pattern, line):
                output_file.write(line)

def main():
    input_log_path = '../logs/mastodon-web.log'
    output_log_path = 'steven_inbox_posts.log'
    
    filter_log_file(input_log_path, output_log_path)
    
    print(f"Filtering complete. Matching logs written to {output_log_path}")

if __name__ == "__main__":
    main()
