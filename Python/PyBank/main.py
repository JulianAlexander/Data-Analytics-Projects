import csv
import os
with open(r'C:\Users\thela\OneDrive\UCB Data Bootcamp\Homework #3\budget_data_1.csv',newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    num_months = list(csvreader)
    row_count = len(num_months)
    print("Financial Analysis")
    print("-----------------------------------")
    print("Number of months: " + str(row_count))
    new_list = (list(csvreader))
    rev = 0
    for row in num_months:
        rev += float((row[1]))
    print("Total Revenue: $" + str(rev))
    tot_rev = str(rev)
    avg = round(rev / (row_count),2)
    print("Average Revenue Change: $" + str(avg))
    answer = max(num_months, key=lambda column: int(column[1]))
    print("Greatest increase in revenue: " + answer[0] + " $" + answer[1])
    answer2 = min(num_months, key=lambda column: int(column[1]))
    print("Greatest decrease in revenue: " + answer2[0] + " $"+answer2[1])

output_dict = {
    "Financial Analysis" : '',
    "-------------------------------------":'',
    "Number of months: ": str(row_count),
    "Total Revenue: $" : str(rev),
    "Average Revenue Change: $" : str(avg),
    "Greatest increase in revenue: ": answer[0] + " $" + answer[1],
    "Greatest decrease in revenue: ": answer2[0] + " $" + answer2[1]
}
cleaned_csv = zip(output_dict.keys(),output_dict.values())
output_file = os.path.join("Revenue_Summary.csv")
with open(output_file,"w",newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerows(cleaned_csv)
    
