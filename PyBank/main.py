#Note:  for some reason, my average change is much greater than the example.
        #I think it is because there is something that gives it a different value when I defined it
        #However, everything else is the same

        #Below is my output (matches with terminal and .txt file)
        
        #Financial Analysis
        #---------------------------------------
        #Total Months: 86
        #Total: $38382578.0
        #Average Change: $671099.0
        #Greatest Increase in Profits: Feb-2012 $1926159.0
        #Greatest Decrease in Profits: Sep-2013 $-2196167.0

import os
import csv

#Read/open csv
with open('PyBank_budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)
    #print(csvreader)

    #Declare/initialize variables
    totalFinances = 0
    profitLossDiff = 0
    lastProfitLossDiff = 0
    greatestInc = 0
    greatestIncMonth = " "
    greatestDec = 0
    greatestDecMonth = " "
    averageFinChange = []
    rowCounter = 0 #counts each row in the csv

    #Loop through csv
    for row in csvreader:
        #print(row)
        rowCounter = rowCounter + 1
        #rowCounter = sum(1 for row in csvreader( open ('PyBank_budget_data.csv')))
        totalFinances += float(row[1])
        profitLossDiff = float(row[1]) - lastProfitLossDiff
        lastProfitLossDiff = float(row[1])

        if profitLossDiff > greatestInc:
            greatestInc = profitLossDiff
            greatestIncMonth = row[0]

        if profitLossDiff < greatestDec:
            greatestDec = profitLossDiff
            greatestDecMonth = row[0]
    
    averageFinChange.append(int(row[1]))

averageChange = sum(averageFinChange) / len(averageFinChange)

#Print the finanial analysis

#Answer Key from Gitlab
#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)


##https://stackoverflow.com/questions/7469301/format-int-as-int-but-float-as-3f/7469480 <-- floats
#Print election results
print(" ")
print(f"Financial Analysis")
print(f"---------------------------------------")
print(f"Total Months: {rowCounter}")
print(f"Total: ${totalFinances}")
print(f"Average Change: ${averageChange}")
print(f"Greatest Increase in Profits: {greatestIncMonth} ${greatestInc}")
print(f"Greatest Decrease in Profits: {greatestDecMonth} ${greatestDec}")
print(" ")

#Write to a text file: 
#https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
#https://www.geeksforgeeks.org/reading-writing-text-files-python/ <-- End of Line command /n

file = open("PyBank.txt", 'w')

file.write(" \n")
file.write(f"Financial Analysis \n")
file.write(f"---------------------------------- \n")
file.write(f"Total Months: {rowCounter} \n")
file.write(f"Total: ${totalFinances} \n")
file.write(f"Average Change: {averageChange} \n")
file.write(f"Greatest Increase in Profits: {greatestIncMonth} ${greatestInc} \n")
file.write(f"Greatest Decrease in Profits: {greatestDecMonth} ${greatestDec} \n")
file.write(" \n")

file.close()
#