# Import the os module
import os

# Module for reading CSV files
import csv

# Path to the csvfile
election_data = os.path.join('Resources', 'election_data.csv')

# Initialize variables 
total_votes = 0 
votes_per_candidate = {}

# Open election_data
with open(election_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Read each row of data after header
    for row in csvreader:
        total_votes += 1
        if row[2] in votes_per_candidate:
            votes_per_candidate[row[2]] += 1
        else:
            votes_per_candidate[row[2]] = 1   
        
        

# Print all Values
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")

for candidate, votes in votes_per_candidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/total_votes) + " (" +  str(votes) + ")")
    
print("-------------------------") 

winner = max(votes_per_candidate, key=votes_per_candidate.get)

print(f"Winner: {winner}")

# Write output file

pypoll = open("election_results.txt", "w")
pypoll.write("Election Results")
pypoll.write('\n')
pypoll.write("-------------------------")
pypoll.write('\n')
pypoll.write("Total Votes: " + str(total_votes))
pypoll.write('\n')
pypoll.write("-------------------------")
pypoll.write('\n')

for candidate, votes in votes_per_candidate.items():
    pypoll.write(candidate + ": " + "{:.3%}".format(votes/total_votes) + "   (" +  str(votes) + ")")
    pypoll.write('\n')
  
pypoll.write("-------------------------") 
pypoll.write('\n')
pypoll.write(f"Winner: {winner}")
pypoll.write('\n')