import csv
import statistics

category_rev = {}
revenues = []

top_product = ""
top_rev = 0

total_rev = 0

with open(r"C:\Users\daler\Desktop\Projects\DaleLuis Persistent training\file operations\Q3\sales.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        product = row["product"]
        category = row["category"]
        quantity = int(row["quantity"])
        unit_price = float(row["unit_price"])

        rev = quantity * unit_price
        revenues.append(rev)
        total_rev += rev

        if category in category_rev:
            category_rev[category] += rev
        else:
            category_rev[category] = rev

        if rev > top_rev:
            top_rev = rev
            top_product = product

avg = statistics.mean(revenues)

print("=== Sales Report ===")
print("Revenue by Category:")

for category, revenue in category_rev.items():
    print(f"{category}: {revenue:.2f}")

print()
print(f"Top Product : {top_product} ({top_rev})")
print(f"Total Revenue : {total_rev}")
print(f"Avg / Txn : {avg}")