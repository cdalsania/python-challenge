# Import dependencies
import os
import csv

election_data = os.path.join("election_data.csv")

# Define variables
# names of candidates
candidates = []

# number of votes each candidate receives
num_votes = []

# percentage of total votes each candidate garners 
percent_votes = []

# total number of votes
total_votes = 0

#Reading the header row
with open(election_data, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    for row in csvreader:
        #vote-counter 
        total_votes += 1 