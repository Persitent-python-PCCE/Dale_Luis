from collections import Counter
import log_utils

entries = log_utils.read_logs(r"C:\Users\daler\Desktop\Projects\DaleLuis Persistent training\file operations\Q1\app.log")
counter = Counter()
errors = []

for level, message in entries:
    counter[level] += 1

    if level == "ERROR":
        errors.append(message)
        
print("=== Log Summary ===")
print(f"INFO    : {counter['INFO']}")
print(f"WARNING : {counter['WARNING']}")
print(f"ERROR   : {counter['ERROR']}")
print(f"DEBUG   : {counter['DEBUG']}")
print("\nErrors found:\n")
for err in errors:
    print(f"- {err}")

with open(r"C:\Users\daler\Desktop\Projects\DaleLuis Persistent training\file operations\Q1\log_summary.txt", "w") as f:
    f.write("=== Log Summary ===\n")
    f.write(f"INFO    : {counter['INFO']}\n")
    f.write(f"WARNING : {counter['WARNING']}\n")
    f.write(f"ERROR   : {counter['ERROR']}\n")
    f.write(f"DEBUG   : {counter['DEBUG']}\n")

    f.write("\nErrors found:\n")
    for error in errors:
        f.write(f"- {error}\n")