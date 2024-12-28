# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Define the file path
file_path = r'C:\Users\stona\OneDrive\Desktop\Module 3 challenge\python-challenge\PyBank\Resources\budget_data.csv' 

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Initialize variables to track the financial data
months = []
total_months = 0
total_net = 0
previous_net = None
net_change_list = []
changes = []
profit_losses = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999]

# Open and read the CSV file
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header row

    # Extract the first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    # Process each row of data
    for row in reader:
        print(row)  # Print each row for debugging purposes 

        # Ensure there are no empty rows or incorrect data
        if len(row) < 2:
            continue

        months.append(row[0])
        try:
            profit_losses.append(int(row[1]))
        except ValueError:
            # Handle the case where conversion to int fails 
            print(f"Error converting {row[1]} to integer. Skipping this row.")
            continue

        # Track the total
        total_months += 1
        total_net += int(row[1])

        # Track the net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)

        # Calculate the greatest increase in profits
        if net_change > greatest_increase[1]:
            greatest_increase = [row[0], net_change]

        # Calculate the greatest decrease in profits
        if net_change < greatest_decrease[1]:
            greatest_decrease = [row[0], net_change]

# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output_summary = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
)

# Print the output
print(output_summary)

# Write the results to a text file
with open(file_to_output, mode='w') as txt_file:
    txt_file.write(output_summary)
