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

print(total_votes , candidate_options)
