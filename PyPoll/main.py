# importing modul to work with csv file
import csv

# defining variables
total_votes = 0
set_candidate = {}

# creating file path
file_path = '../PyPoll/Resources/election_data.csv'

#open the csv file 
with open(file_path, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
     
     # seperating header
    svhead = next(csvreader)

    #looping for all row    
    for row in csvreader:

        # The total number of votes cast
        total_votes +=1

        # check if there is new canditate and add if so
        if row[2] not in set_candidate:

         #  A complete list of candidates who received votes and The total number of votes each candidate won
            set_candidate[row[2]] = 1
        else:
            set_candidate[row[2]] += 1    

print(f''' ```text
  Election Results
-------------------------
  Total Votes: {total_votes}
-------------------------''')            
#  The percentage of votes each candidate won
for candidate, vote in set_candidate.items():

    print(f'{candidate}: {round(((vote/total_votes)*100),3)}% ({vote})')

print('__________________________')
print('\n')
#  The winner of the election based on popular vote.
winner = max(set_candidate, key = set_candidate.get)      
print(f'winner: {winner}')
print('_________________________')
print('\n')
print('````')


pypoll = 'analysis/pypoll.txt'
with open(pypoll,'w') as outfile:
    outfile.write(f''' ```text
  Election Results
-------------------------
  Total Votes: {total_votes}
-------------------------\n''')
    for candidate, vote in set_candidate.items():
        outfile.write(f'{candidate}: {round(((vote/total_votes)*100),3)}% ({vote})')
        outfile.write('\n')
    outfile.write('__________________________')
    outfile.write('\n')
    outfile.write(f'winner: {winner}')
    outfile.write('\n')
    outfile.write('````')