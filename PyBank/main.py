import csv

csvpath = "Resources/pyBankData.csv"
file_to_output = "analysis/budget_analysis_1.txt"

months = 0 
netProfitOrLosses = 0
monthOfChange = []
previousRevenue = 0
revChangeList = []
revChange = 0
revAverage = 0
greatestIncrease = ["", 0]
greatestDecrease = ["", 9999999999999999999]
totalRevenue = 0

with open (csvpath) as revenuData:
    reader = csv.DictReader(revenuData)
 
    for row in reader: 
        months = months + 1
        netProfitOrLosses = netProfitOrLosses + int(row["Profit/Losses"])

        revChange = int(row["Profit/Losses"]) - previousRevenue
        previousRevenue = int(row["Profit/Losses"])
        revChangeList = revChangeList + [revChange]
        monthOfChange = monthOfChange + [row["Date"]]

        if (revChange > greatestIncrease[1]): 
            greatestIncrease[0] = row["Date"]
            greatestIncrease[1] = revChange

        if (revChange < greatestDecrease[1]): 
            greatestDecrease[0] = row["Date"]
            greatestDecrease[1] = revChange

revAverage = sum(revChangeList) / len(revChangeList)

output = (
    f"\nFinanical Analysis\n"
    f"------------------------------------------------\n"
    f"Total Months:  {months}\n"
    f"Total Revenue: ${netProfitOrLosses}\n"
    f"Average Revenue Change: ${revAverage}\n"
    f"Greatest Increase in Revenue: {greatestIncrease[0]} (${greatestIncrease[1]})\n"
    f"Greatest Decrease in Revenue: {greatestDecrease[0]} (${greatestDecrease[1]})\n"
)

print(output)

with open(file_to_output, "w") as txt_file: 
    txt_file.write(output)