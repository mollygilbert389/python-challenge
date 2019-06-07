import csv

csvpath = "Resources/pyBankData.csv"

months = 0
monthsArray = {}
netProfitOrLosses = 0
netProfitOrLossesArray = []
averageProfitOrLosses = 0
averageChangeProfitOrLosses = 0
greatestIncrease = 0
greatestDecrease = 0

with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

## Month counter
    for row in csvreader: 
        netProfitOrLossesArray.append(row[1])
        monthsArray[months] = row
        months = months+1

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
averageProfitOrLosses = column / netProfitOrLosses
## 1st(A) number to second(B) number for 43 number pairs then take their number and add them all up
## calculate difference between number A and B = c
## push that number into an array 
## caluclate the sum of that array
## divide the increase by the original number and multiply by 100*
print("Average Change:", averageProfitOrLosses)

## Prints Greatest Increase

## Prints Greatest Decrease