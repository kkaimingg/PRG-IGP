from pathlib import Path
import csv

# create a file path to the CSV file.
def overheads_finder():
    fp = Path.cwd()/"csv_reports" / "overheads-day-90.csv"

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
                max_overhead_category=max_overhead_category.upper()

    return(max_overhead_category , max_overheads)
# # Print the result for checking
# if max_overhead_category is not None:
#     print(f"[HIGHEST OVERHEAD] {max_overhead_category}: {max_overheads}%")
# else:
#     print("No data found.")




