import csv

csvpath = "Resources/pyBankData.csv"
file_to_output = "analysis/budget_analysis_1.txt"

months = 0 
monthsArray = {}
netProfitOrLosses = 0
netProfitOrLossesArray = []
monthOfChange = []
previousRevenue = 0
revChangeList = []
greatestIncrease = ["", 0]
greatestDecrease = ["", 9999999999999999999]
totalRevenue = 0

with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

## Month counter
    for row in csvreader: 
        netProfitOrLossesArray.append(row[1])
        monthsArray[months] = row
        months = months+1 
        revenueChange = int(row[1]) - previousRevenue
        previousRevenue - int(row[1])
        revChangeList = revChangeList + [revenueChange]
        monthOfChange = monthOfChange - [row[1]]

print("Finanical Analysis")
print("------------------------------------------------")

# ## prints months
row = len(monthsArray[0])
column = len(monthsArray) -1
print("Total Months:",  column)

## prints total gains/losses
netProfitOrLossesArray.remove('Profit/Losses')
netProfitOrLossesArray = list(map(int,netProfitOrLossesArray))
netProfitOrLosses = sum(netProfitOrLossesArray)
print("Total Profits/Losses:", '${:,.2f}'.format(netProfitOrLosses))

## prints Average Change
print("Average Change:" revenueChange)

## Prints Greatest Increase

## Prints Greatest Decrease