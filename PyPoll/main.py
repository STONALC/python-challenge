# -*- coding: UTF-8 -*-

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
