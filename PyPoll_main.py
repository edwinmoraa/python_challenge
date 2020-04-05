#modernize the vote-counting process
#total number of votes cast
#complete list of candidates who got votes
#percentage of votes each candidate won
#winner of election of election based on popular votes
#make a txt file again

import os
import csv



csv_path = os.path.join("election_data.csv")
print('Election Results')
print('----------------')
votes = []
candidates = []

with open(csv_path, newline='') as csv_file:
    csvreader = csv.reader(csv_file,delimiter = ',')
print(csvreader)
csv_header = next(csvreader)
print(f'csv header: {csv_header}')
for column in csvreader:
    votes.append(column[0])
    candidates.append(column[2])

total_votes = (len(votes))
print(f'Total Votes: {total_votes}')

#candidates
Khan = int(candidates.count('Khan'))
Correy = int(candidates.count('Corey'))
Li = int(candidates.count('Li'))
O_Tooley = int(candidates.count("O'Tooley"))

#percentage
Khan_pct = (Khan/total_votes) * 100
Correy_pct = (Correy/total_votes) * 100
Li_pct = (Li/total_votes) * 100
O_Tooley_pct = (O_Tooley/total_votes) * 100

print(f'Khan: {Khan_pct}% {Khan}')
print(f'Correy: {Correy_pct}% {Correy}')
print(f'Li: {Li_pct}% {Li}')
print(f"O'Tooley: {O_Tooley_pct}% {O_Tooley}")

#winner

if Khan > Correy > Li > O_Tooley:
    winner = 'Khan'
elif Correy > Khan > Li > O_Tooley:
    winner = 'Correy'
elif Li > Khan > Correy > O_Tooley:
    winner = 'Li'
elif O_Tooley > Khan > Correy > Li:
    winner = "O'Tooley"
    print(f'Winner: {winner}')

# save as txt
txt_path = os.path.join('election.txt')
with open(txt_path, 'w', newline='') as txtfile:
    txtfile.write(f'Total Votes: {total_votes}')
    txtfile.write(f'Khan: {Khan_pct}% {Khan})')
    txtfile.write(f'Correy: {Correy_pct}% {Correy})')
    txtfile.write(f'Li: {Li_pct}% {Li})')
    txtfile.write(f" O'Tooley: {O_Tooley_pct}% {O'Tooley}) ")
    txtfile.write(f'Winner: {Winner}')
txtfile.close()












#txt file
writer = csv.writer(election_txt)
writer.writerow([

])
