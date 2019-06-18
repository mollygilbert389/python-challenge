import csv
import operator

csvpath = "PyPollData.csv"
file_to_output = "analysis/PollData.txt"

totalVotes = 0
khanVotes = 0
khanPercentage = 0
correyVotes = 0
correyPercentage = 0
liVotes = 0
liPercentage = 0
otooleyVotes = 0
otooleyPercentage = 0
highestVote = ""
result = 0


with open (csvpath) as pollData:
    reader = csv.DictReader(pollData)

    for row in reader: 
        totalVotes = totalVotes + 1
        
        if (row["Candidate"] == "Khan"):
            khanVotes = khanVotes + 1
            khanPercentage = khanVotes / totalVotes
            khanPercentage = khanPercentage * 100
        if (row["Candidate"] == "Correy"):
            correyVotes = correyVotes + 1
            correyPercentage = correyVotes /totalVotes
            correyPercentage = correyPercentage * 100
        if (row["Candidate"] == "Li"):
            liVotes = liVotes + 1
            liPercentage = liVotes / totalVotes
            liPercentage = liPercentage * 100
        if (row["Candidate"] == "O'Tooley"):
            otooleyVotes = otooleyVotes + 1
            otooleyPercentage = otooleyVotes / totalVotes
            otooleyPercentage = otooleyPercentage * 100

candidates = {
    "Khan" : khanVotes,
    "Correy" : correyVotes,
    "Li" : liVotes,
    "O'Tooley" : otooleyVotes
}

winner = max(candidates.items(), key=operator.itemgetter(1))[0]


output = (
    "\nElection Results\n"
    "---------------------------------\n"
    f"Total Votes: {totalVotes}\n"
    "---------------------------------\n"
    f"Khan: {khanPercentage:.2f}% ({khanVotes})\n"
    f"Correy: {correyPercentage:.2f}% ({correyVotes})\n"
    f"Li: {liPercentage:.2f}% ({liVotes})\n"
    f"O'Tooley: {otooleyPercentage:.2f}% ({otooleyVotes})\n"
    "---------------------------------\n"
    f"Winner: {winner}\n"
    "---------------------------------\n"
)

print(output)