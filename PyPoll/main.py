# -*- coding: UTF-8 -*-

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidates = {}
candidate_list = []
winner = []

# Define lists and dictionaries to track candidate names and vote counts
total_votes = 0
total_vote_count = 0
candidates = []
candidate_list = len 
percentage_votes = 0
winner = ""
winning_count = 0
winner_summary = []
candidates_list = {}
winner_name = []

# Winning Candidate and Winning Count Tracker
winner_candidate = winner
winning_count = winning_count 


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        total_votes += 1
    candidate = row[2]
    
    index = len(candidates_list)  
    value = candidate  
    

        # Print a loading indicator (for large datasets)
    print(". ", end="")

        # Increment the total vote count for each row
    total_vote_count += 1


        # Get the candidate's name from the row
    for row in reader:
            winner_name = row[2]  # Assuming candidate's name is in the third column
    print(winner_name)



        # If the candidate is not already in the candidate list, add them
    candidate_name = row[2]  
    if isinstance(candidate_list, (list, set, tuple)):
         if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
    
        # Add a vote to the candidate's count
   

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(total_votes)


    # Write the total vote count to the text file
    total_vote_count = f"Total Vote Count: {total_votes}/n"


    # Loop through the candidates to determine vote percentages and identify the winner
    print("Candidate Vote Percentages:")
    vote_percentage = (total_votes / total_votes) * 100
    print(f"{candidate}: {vote_percentage:.2f}%")


        # Get the vote count and calculate the percentage


        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage
    print(f"Total Votes: {total_votes}")
    print("Candidate List:", candidate_list)
    for candidate in candidates:
            print(f"{candidate}: {percentage_votes[candidate]:.2f}% ({candidates[candidate]})")
            print(f"Winner: {winner}")

    # Generate and print the winning candidate summary
print(f"The winning candidate is {winner} with {total_vote_count}")


    # Save the winning candidate summary to the text file


