import csv
import os

csvpath = "Resources/pyBankData.csv"
file_to_output = "analysis/budget_analysis_1.txt"

months = 0 
netProfitOrLosses = 0
monthOfChange = []
revChangeList = []
greatestIncrease = ["", 0]
greatestDecrease = ["", 9999999999999999999]


with open (csvpath) as revenuData:
    reader = csv.reader(revenuData)

    header = next(reader)
    first_row = next(reader)
    previousRevenue = int(first_row[1])
 
    for row in reader: 
        months = months + 1
        netProfitOrLosses = netProfitOrLosses + int(row[1])


        revChange = int(row[1]) - previousRevenue
        previousRevenue = int(row[1])
        revChangeList = revChangeList + [revChange]
        monthOfChange = monthOfChange + [row[0]]

        if (revChange > greatestIncrease[1]): 
            greatestIncrease[0] = row[0]
            greatestIncrease[1] = revChange

        if (revChange < greatestDecrease[1]): 
            greatestDecrease[0] = row[0]
            greatestDecrease[1] = revChange

revAverage = sum(revChangeList) / len(revChangeList)

output = (
    f"\nFinanical Analysis\n"
    f"------------------------------------------------\n"
    f"Total Months:  {months}\n"
    f"Total Revenue: ${netProfitOrLosses}\n"
    f"Average Revenue Change: ${revAverage:.2f}\n"
    f"Greatest Increase in Revenue: {greatestIncrease[0]} (${greatestIncrease[1]})\n"
    f"Greatest Decrease in Revenue: {greatestDecrease[0]} (${greatestDecrease[1]})\n"
)

print(output)

with open(file_to_output, "w") as txt_file: 
    txt_file.write(output)