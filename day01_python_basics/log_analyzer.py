import json
from collections import defaultdict

LOG_FILE = "sample.log"
OUTPUT_FILE = "summary.json"

def analyze_logs(file_path):
    #error_counts = defaultdict(int)
    #warning_counts = defaultdict(int)
    #info_counts = defaultdict(int)
    results = defaultdict(lambda: defaultdict(int))

    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()

                #if line.startswith("ERROR"):
                 #   message =line.replace("ERROR", "").strip()
                  #  error_counts[message] += 1
                #elif line.startswith("WARNING"):
                 #   message = line.replace("WARNING", "").strip()
                  #  warning_counts[message] += 1
                #elif line.startswith("INFO"):
                 #   message = line.replace("INFO", "").strip()
                  #  info_counts[message] += 1
                if not line:
                    continue
                #Split only at first space
                parts = line.split(" ", 1)
                if len(parts) != 2:
                    continue
                level = parts[0].upper()
                message = parts[1].strip()
                results[level][message] += 1
    except FileNotFoundError:
        print("Log file not found.")
        return {}
    
    return results

def print_summary(results):
    for level, messages in results.items():
        print(f"\n{level} Summary:")
        total = 0
        max_count = 0
        most_frequent = ""
        for message, count in messages.items():
            print(f"{message}: {count}")
            total += count
            if count > max_count:
                max_count = count
                most_frequent = message
        print(f"Total {level}: {total}")
        if most_frequent:
            print(f"Most frequent {level}: {most_frequent} ({max_count} times)")
def save_summary_to_json(results):
    # Convert defaultdict to normal dict for clean JSON
    clean_results = {
        level: dict(messages)
        for level, messages in results.items()
    }
    with open(OUTPUT_FILE, "w") as json_file:
        json.dump(results, json_file, indent=4)

if __name__ == "__main__":
    result = analyze_logs(LOG_FILE)
    print_summary(result)
    save_summary_to_json(result)