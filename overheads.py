from pathlib import Path
import csv

# create a file path to the CSV file.
fp = Path.cwd() / "overheads-day-90.csv"

# Open and read the CSV file.
with open(fp, 'r', newline='') as csvfile:
    # Create a CSV reader object.
    csv_reader = csv.reader(csvfile)
    
    # Skip header
    next(csv_reader)

    # Create variables to track the highest overheads
    max_overheads = float('-inf')  
    # Initialize with negative infinity
    max_overhead_category = None

    # Iterate through the rows in the CSV file.
    for row in csv_reader:
        # Assuming the second column contains overheads
        category = row[0]
        overheads = float(row[1])  # Convert to float for numeric comparison

        # Check if the current overheads are higher than the current maximum
        if overheads > max_overheads:
            max_overheads = overheads
            max_overhead_category = category

# Print the result
if max_overhead_category is not None:
    print(f"HIGHEST OVERHEADS: {max_overhead_category} with {max_overheads} overheads.")
else:
    print("No data found.")




