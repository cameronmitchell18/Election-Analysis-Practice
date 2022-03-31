# Py poll data set psuedo code 
# 1. Open and review the data set 
# 2. Get the total number of votes cast
# 3. A complete list of canidates who recieved votes 
# 4. The total number of votes each canidate won 
# 5. The winner of the election based on popular vote

import csv
import os

# Assign a variable to load the csv file from path 
file_to_load = os.path.join('Resources' , 'election_results.csv')

# Assign a variable to save the file to a path 
file_to_save = os.path.join('election_analysis' , 'analysis.txt')

# Initalizing a total votes variable to zero 
total_votes = 0 

# Initializing a canadites name list 
candidate_options = []

# Creating an empty dictionary to count the votes of each candidate
candidate_votes = {}

# Variable to hold the winning candidate 
winning_candidate = ''

# Variable for the winning count equal to 0 
winning_count = 0 

# Variable for the winning % equal to 0 
winning_percentage = 0 

# Open the election results and read the file 
with open(file_to_load) as election_data: 

    # To do: read and analyze the data here. 
    # Read the file object with the reader function 
    file_reader = csv.reader(election_data)

    # Read the header row 
    headers = next(file_reader)
    
    # Print each row in the csv file 
    for row in file_reader:
        # Adding to the total count 
        total_votes += 1
        # Getting the candidate from the second index
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #Add it to the list of candidates
            candidate_options.append(candidate_name)

            # Begin Tracking the Candidate's vote count
            candidate_votes[candidate_name] = 0 

            # Add a vote to that candidate's count 
        candidate_votes[candidate_name] += 1

        # Save the results to ur text file
with open(file_to_save, 'w') as txt_file:
    election_results = (
   
        f'\nElection Results\n'
        f'-----------------------\n'
        f'Total Votes: 369,711\n'
        f'----------------------\n')

    print(election_results, end = '')

    #Save the finale vote count to the text file
    txt_file.write(election_results)



    # Detrmine the percenatge of votes for each candidate by looping through the counts
    # 1. Iterate through the candidate list 
    for candidate_name in candidate_votes:
        #2. Retrive vote count of a candidate 
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes 
        vote_percentage = float(votes) / float(total_votes) * 100
        #4. print the candidate name and % of votes 
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #print(f'{candidate_name}: received {vote_percentage:.1f}% of the votes.')
        #determine if the votes is greate than the winning count 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote %
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    #winning_candidate_summary = (
        #f"-------------------------\n"
        #f"Winner: {winning_candidate}\n"
        #f"Winning Vote Count: {winning_count:,}\n"
        #f"Winning Percentage: {winning_percentage:.1f}%\n"
        #f"-------------------------\n")
    #print(winning_candidate_summary)


