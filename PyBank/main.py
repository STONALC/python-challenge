# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os
file_path = '/path/to/your/budget_data.csv'

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path
with open('/path/to/your/budget_data.csv', mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)
# Define variables to track the financial data
months = 0
total_months = 0
total_net = 0
net_total = 0
previous_net = 0
output = 0
month_of_change = []
changes = []
profit_losses = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999]
# Add more variables to track other necessary financial data
for row in reader:
    months.append(row[0])
    profit_losses.append(int(row[1]))
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    

    # Track the total and net change
    total_months += 1
    total_net += int(row[1])
    previous_net += int(row[1])

    # Process each row of data
    for row in reader:
        months.append(row[0])
        profit_losses.append(int(row[1]))
    
        # Track the total
        total_months += 1
        total_net += int(row[1])

        # Track the net change


        # Calculate the greatest increase in profits (month and amount)
        greatest_increase = max(changes)
        greatest_increase_date = months[changes.index(greatest_increase) +1]

        # Calculate the greatest decrease in losses (month and amount)
        greatest_decrease = min(changes)
        greatest_decrease_date = months[changes.index(greatest_decrease) +1]


# Calculate the average net change across the months
average_change = sum(changes) / len(changes)

# Generate the output summary
output_summary =(f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Net Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Print the output
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_Total}") 
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest_increase in Profits: {greatest_increase_date} (${greatest_increase}")
print(f"Greatest_decrease in Profits: {greatest_decrease_date} (${greatest_decrease}")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
