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

# Open the election results and read the file 
with open(file_to_load) as election_data: 

    # To do: read and analyze the data here. 

    # Read the file object with the reader function 
    file_reader = csv.reader(election_data)

    # Print the header row 
    headers = next(file_reader)
    print(headers)

    # Print each row in the csv file 
    #for row in file_reader:
        #print(row)
