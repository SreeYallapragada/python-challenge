
import os
import csv

#Read/open csv
#csvpath = os.path.join('PyPoll','PyPoll_election_data.csv')

#Declare the variables/initialize to 0
totalVotes = 0
votesForKhan = 0
votesForCorrey = 0
votesForLi = 0
votesForOTooley = 0

with open('PyPoll_election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)
#Loop through csv
    for row in csvreader:
        totalVotes += 1
        if row[2] == "Khan":
            votesForKhan += 1
        elif row[2] == "Correy": 
            votesForCorrey += 1
        elif row[2] =="Li":
            votesForLi += 1
        elif row[2] == "O'Tooley":
            votesForOTooley += 1

#Declare/Initialize indeces of values
candidateList = ["Khan", "Correy", "Li", "O'Tooley"]
voteTypes = [votesForKhan, votesForCorrey, votesForLi, votesForOTooley]

#Dictionary of the candidate list and types of votes
votedCandidateDict = dict(zip(candidateList, voteTypes))

#Had problem running dictionary, inserted a key after reading link
#https://www.geeksforgeeks.org/python-dictionary-keys-method/

#Create key for dictionary
key = max(votedCandidateDict, key = votedCandidateDict.get)

#Redefine candidate variables to calculate individual election result
percentKhan = (votesForKhan/totalVotes) * 100 #%
percentCorrey = (votesForCorrey/totalVotes) * 100 #%
percentLi = (votesForLi/totalVotes) * 100 #%
percentOTooley = (votesForOTooley/totalVotes) * 100 #%


#Answer Key from Gitlab
#
#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------
#

#https://stackoverflow.com/questions/7469301/format-int-as-int-but-float-as-3f/7469480 <-- floats
#https://www.geeksforgeeks.org/reading-writing-text-files-python/ <--- End of Line /n
#Print election results
print(" ")
print(f"Election Results")
print(f"-----------------------------")
print(f"Total Votes: {totalVotes}")
print(f"-----------------------------")
print(f"Khan: {percentKhan:.3f}% ({votesForKhan})")
print(f"Correy: {percentCorrey:.3f}% ({votesForCorrey})")
print(f"Li: {percentLi:.3f}% ({votesForLi})")
print(f"O'Tooley: {percentOTooley:.3f}% ({votesForOTooley})")
print(f"-----------------------------")
print(f"Winner: {key}")
print(f"-----------------------------")
print(" ")

#Write to a text file: 
#https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
file = open("PyPoll.txt", 'w')

file.write(" \n")
file.write(f"Election Results \n")
file.write(f"----------------------------- \n")
file.write(f"Total Votes: {totalVotes} \n")
file.write(f"-----------------------------\n")
file.write(f"Khan: {percentKhan:.3f}% ({votesForKhan}) \n")
file.write(f"Correy: {percentCorrey:.3f}% ({votesForCorrey}) \n")
file.write(f"Li: {percentLi:.3f}% ({votesForLi}) \n")
file.write(f"O'Tooley: {percentOTooley:.3f}% ({votesForOTooley}) \n")
file.write(f"----------------------------- \n")
file.write(f"Winner: {key} \n")
file.write(f"----------------------------- \n")
file.write(" \n")

file.close()
#