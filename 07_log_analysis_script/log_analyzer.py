import os
import glob
import re

def count_occurrences(content: str, pattern: str) -> int:
    """Return the number of non‑overlapping occurrences of *pattern* in *content*, case‑insensitive.
    Excludes lines containing "CRCcheck OK" and "CRC error recovered" to avoid false positives.
    The pattern is a simple literal string (e.g. "crc error")."""
    # Remove excluded phrases (case‑insensitive) before counting
    excluded_phrases = ["crccheck ok", "crc error recovered", "no crc error found"]
    for ex in excluded_phrases:
        content = re.sub(re.escape(ex), "", content, flags=re.IGNORECASE)
    return len(re.findall(re.escape(pattern), content, flags=re.IGNORECASE))

def analyze_logs():
    # Find all server*.log files in the current directory
    log_files = sorted(glob.glob("server*.log"))
    if not log_files:
        print("No server*.log files found in the current directory.")
        return

    header = f"{'Server File':<20} | {'CRC Error Count':<15} | {'Link Down Count':<15}"
    separator = "-" * len(header)
    print(header)
    print(separator)

    total_crc = 0
    total_link = 0

    for file_path in log_files:
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            crc_count = count_occurrences(content, "crc error")
            link_count = count_occurrences(content, "link down")
            file_name = os.path.basename(file_path)
            print(f"{file_name:<20} | {crc_count:<15} | {link_count:<15}")
            total_crc += crc_count
            total_link += link_count
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    print(separator)
    print(f"{'Total':<20} | {total_crc:<15} | {total_link:<15}")

if __name__ == "__main__":
    analyze_logs()
