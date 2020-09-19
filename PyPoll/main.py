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

#if candidate is not on list, add the name to the list, along with the vote name
#if candidate is already on the list, just add the vote to that name

    if row[2] not in candidates:
        candidates.append(row[2])
        index = candidates.index(row[2])
        num_votes.append(1)
    else:
        index = candidates.index(row[2])
        num_votes[index] += 1

        #percent_votes list 
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
