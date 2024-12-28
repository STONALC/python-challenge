This is my second submission of the python challenge. In completing this challenge, I reviewed class notes and the past videos covering 
python. I also used microsoft co-pilot and other online sources in completing this task. In particular, the following scripts were written or edited with the aid of microsoft co-pilot:


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

and

# Import necessary modules
import csv
import os

# Define the file paths
file_to_load = r'C:\Users\stona\OneDrive\Desktop\Module 3 challenge\python-challenge\PyPoll\Resources\election_data.csv' 
file_to_output = r'C:\Users\stona\OneDrive\Desktop\Module 3 challenge\python-challenge\PyPoll\analysis\election_analysis.txt'

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidates = {}  # Dictionary to store candidate names and vote counts
candidate_list = []  # List to store candidate names

# Open the CSV file and process it
with open(file_to_load, mode='r') as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        total_votes += 1
        candidate_name = row[2]  # Assuming candidate's name is in the third column

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates[candidate_name] = 0

        # Add a vote to the candidate's count
        candidates[candidate_name] += 1

# Calculate vote percentages and determine the winner
winning_candidate = ""
winning_count = 0
results = []

for candidate, votes in candidates.items():
    # Calculate the percentage of votes for each candidate
    vote_percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {vote_percentage:.2f}% ({votes})")

    # Update the winning candidate if this one has more votes
    if votes > winning_count:
        winning_count = votes
        winning_candidate = candidate

# Generate the output summary
output_summary = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n"
)

output_summary += "\n".join(results)
output_summary += (
    f"\n----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"----------------------------\n"
)

# Print the output to the terminal
print(output_summary)

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    # Write the results to the text file
    txt_file.write(output_summary)

    # Write the total vote count to the text file
    txt_file.write(f"Total Vote Count: {total_votes}\n")

