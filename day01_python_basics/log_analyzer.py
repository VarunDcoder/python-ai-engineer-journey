import json
from collections import defaultdict

LOG_FILE = "sample.log"
OUTPUT_FILE = "summary.json"

def analyze_logs(file_path):
    error_counts = defaultdict(int)
    warning_counts = defaultdict(int)
    info_counts = defaultdict(int)

    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()

                if line.startswith("ERROR"):
                    message =line.replace("ERROR", "").strip()
                    error_counts[message] += 1
                elif line.startswith("WARNING"):
                    message = line.replace("WARNING", "").strip()
                    warning_counts[message] += 1
                elif line.startswith("INFO"):
                    message = line.replace("INFO", "").strip()
                    info_counts[message] += 1
    except FileNotFoundError:
        print("Log file not found.")
        return {}
    
    return {
        "ERROR": error_counts,
        "WARNING": warning_counts,
        "INFO": info_counts
    }
def print_summary(results):
    for level, messages in results.items():
        print(f"\n{level} Summary:")
        for message, count in messages.items():
            print(f"{message}: {count}")

def save_summary_to_json(results):
    with open(OUTPUT_FILE, "w") as json_file:
        json.dump(results, json_file, indent=4)

if __name__ == "__main__":
    result = analyze_logs(LOG_FILE)
    print_summary(result)
    save_summary_to_json(result)