import json
from collections import defaultdict

LOG_FILE = "sample.log"
OUTPUT_FILE = "summary.json"

def analyze_logs(file_path):
    error_counts = defaultdict(int)

    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()

                if line.startswith("ERROR"):
                    error_type =line.replace("ERROR", "").strip()
                    error_counts[error_type] += 1
    except FileNotFoundError:
        print("Log file not found.")
        return {}
    
    return error_counts

def print_summary(error_counts):
    print("\nError Summary:")
    for error, count in error_counts.items():
        print(f"{error}: {count}")

def save_summary_to_json(error_counts):
    with open("summary.json", "w") as json_file:
        json.dump(error_counts, json_file, indent=4)

if __name__ == "__main__":
    result = analyze_logs(LOG_FILE)
    print_summary(result)
    save_summary_to_json(result)