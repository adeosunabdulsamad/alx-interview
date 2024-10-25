#!/usr/bin/python3
"""
The module for the project 
"""
import sys

total_size = 0
status_counts = {}
valid_statuses = [200, 301, 400, 401, 403, 404, 405, 500]
line_count = 0

def print_stats():
    """
    function to print stats
    """
    print(f"File size: {total_size}")
    for status in sorted(status_counts):
        if status_counts[status]:
            print(f"{status}: {status_counts[status]}")

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue
        
        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
        except (ValueError, IndexError):
            continue

        total_size += file_size
        if status_code in valid_statuses:
            status_counts[status_code] = status_counts.get(status_code, 0) + 1
        
        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
