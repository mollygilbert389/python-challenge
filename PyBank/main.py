import csv

csvpath = "Resources/pyBankData.csv"

months = 0
monthsArray = {}
netProfitOrLosses = 0
netProfitOrLossesArray = [0]
averageProfitOrLosses = 0
averageChangeProfitOrLosses = 0
greatestIncrease = 0
greatestDecrease = 0

with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

## Month counter
    for row in csvreader: 
        monthsArray[months] = row
        months = months+1

## Net Profit/Losses Counter
    for row in csvreader: 
        netProfitOrLossesArray.append(int(row[1]))



print("Finanical Analysis")
print("------------------------------------------------")

# ## prints months
row = len(monthsArray[0])
column = len(monthsArray) -1
print("Total Months: " +  str(column))

## prints total gains/losses
netProfitOrLosses = sum(map(int, netProfitOrLossesArray))
print(netProfitOrLosses)
# print("Total: " + str(total))


## prints Average Change

## Prints Greatest Increase

## Prints Greatest Decrease