import csv

# Function to read input from CSV and create another file
def process_csv(input_file, output_file):
    with open(input_file, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        # Assuming the CSV has headers, you can skip them if needed
        next(reader)  # Skip header
        with open(output_file, 'w', newline='') as output:
            writer = csv.writer(output)
            for row in reader:
                # Process each row as needed, here we are just copying the rows
                writer.writerow(row)
    print("File processing completed.")

# Usage example
input_file = 'numbers.csv'  # Path to your input CSV file
output_file = 'output.csv'  # Path to the output file you want to create

process_csv(input_file, output_file)