import glob
import os
import re
from collections import defaultdict

# Directory containing log files
log_dir = r'D:/AWS-DCO-GenAI-Portfolio'

# Pattern for server log files
log_pattern = os.path.join(log_dir, 'server*.log')

# Initialize counters per server
counters = defaultdict(lambda: {'CRC error': 0, 'Link Down': 0})

# Regular expressions for the messages
crc_regex = re.compile(r'CRC error', re.IGNORECASE)
link_regex = re.compile(r'Link Down', re.IGNORECASE)

for log_path in glob.glob(log_pattern):
    server_name = os.path.splitext(os.path.basename(log_path))[0]  # e.g., server01
    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if crc_regex.search(line):
                    counters[server_name]['CRC error'] += 1
                if link_regex.search(line):
                    counters[server_name]['Link Down'] += 1
    except Exception as e:
        print(f'Failed to read {log_path}: {e}')

# Print results
print('Error counts per server:')
for server, counts in sorted(counters.items()):
    print(f"{server}: CRC error={counts['CRC error']}, Link Down={counts['Link Down']}")
