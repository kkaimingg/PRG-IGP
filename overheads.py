from pathlib import Path
import csv

# create a file path to the CSV file.
fp = Path.cwd() / "C:\\Users\\jaime\\Downloads\\overheads-day-90.csv"

# Open and read the CSV file.
with open(fp, 'r', newline='') as csvfile:
    # Create a CSV reader object.
    csv_reader = csv.reader(csvfile)
    
    # Skip header
    next(csv_reader)

    # Create an empty list for overheads
    overheads_list = []

    # Iterate through the rows in the CSV file.
    for row in csv_reader:
        # Assuming the second column contains overheads
        overheads_list.append({
            'Category': row[0],
            'Overheads': float(row[1])  # Convert to float for numeric comparison
        })

# Find the category with the highest overheads
highest_overhead_category = max(overheads_list, key=lambda x: x['Overheads'])

# Print the result
print(f"The category with the highest overheads is: {highest_overhead_category['Category']} with {highest_overhead_category['Overheads']} overheads.")


