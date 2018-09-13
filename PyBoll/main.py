#PyBoll
import os
import csv


file = 'election_data.csv'

with open(file, encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)

    #declaring variables
    total_votes = 0
    dict_candidates = {}  #dictionary for candidate votes
    winning_vote_count = 0

    csv_header = next(csvreader)

    for row in csvreader:
#this simply adds up the number of rows of information
#or could us total_votes += 1 if set total_votes = 0
        total_votes += 1

#add up all the votes for each candidate
        candidate_name = row["Candidate"]
        if candidate_name not in dict_candidates:
            dict_candidates[candidate_name] = 1

        else:
            dict_candidates[candidate_name] += 1

print("Election Results")
print("----------------------------")
print("Total Votes: " + str(int(total_votes)))
print("----------------------------")

#determine the winner.  .items --> can loop through all the values and keys
for key,value in dict_candidates.items():
    #loops through every value
    print(key + ": " + str(round(value/total_votes*100, 3)) + "%  (" + str(value) + ")" )

    if value > winning_vote_count:
        winning_vote_count = value
        winner_name = key   #dictionaries are key value pairs
print("----------------------------")
print("Winner: " + winner_name)
print("----------------------------")


#export to text file  (\n creates a line break)
output_file = open('Pypoll Output.txt', 'w')
output_file.write("Election Results  \n")
output_file.write("----------------------------  \n")
output_file.write("Total Votes: " + str(int(total_votes)) + "\n")
output_file.write("----------------------------  \n")
for key,value in dict_candidates.items():
    output_file.write(key + ": " + str(round(value/total_votes*100, 3)) + "%  (" + str(value) + ")" + "\n")
output_file.write("----------------------------  \n")
output_file.write("Winner: " + winner_name + "\n")
output_file.write("----------------------------  \n")
output_file.close()
