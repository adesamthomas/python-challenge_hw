#PyBank

import csv
import sys

file = '../budget_data.csv'

#with open(file, 'r') as budget_data:
#    print(budget_data)
#    lines = budget_data.read()
#    print(lines)

with open(file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    #declaring variables
    total_months = []
    revenue = []
    monthly_change = []
    ave_change = []

#read header row 1st
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")


    for row in csvreader:
        #this simply adds up the number of rows of information, same as total_months = total_months + 1
        #or could us total_months += 1 if set total_months = 0
        total_months.append(row[0])
        #adds up all the revenue for every row (same as total_revenue = total_revenue + int(row[1]))
        #or could use total_revenue += int(row[1]) if set total_revenue = 0
        revenue.append(float(row[1]))
        total_revenue = sum(revenue)

    #find the average change betweens months over the entire period
    for i in range(1,len(revenue)):
        monthly_change.append(revenue[i] - revenue[i-1])
        ave_change = round(sum(monthly_change)/len(monthly_change), 2)

        #find greatest increase and decrease in profits over the entire period
        max_increase = max(monthly_change)
        max_increase_date = str(total_months[monthly_change.index(max(monthly_change))])
        max_decrease = min(monthly_change)
        max_decrease_date = str(total_months[monthly_change.index(min(monthly_change))])

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(len(total_months)))
    print("Total: $" + str(int(total_revenue)))
    print("Average Change: $" + str(ave_change))
    print("Greatest Increase in Profits: " + str(max_increase_date) + " " +" " + "($"+ str(int(max_increase))+ ")")
    print("Greatest Decrease in Profits: " + str(max_decrease_date) + " " +" " + "($"+ str(int(max_decrease))+ ")")

#export to text file  (\n creates a line break)
    output_file = open('Pybank Output.txt', 'w')
    output_file.write("Financial Analysis  \n")
    output_file.write("----------------------------  \n")
    output_file.write("Total Months: " + str(len(total_months)) + "\n")
    output_file.write("Total: $" + str(int(total_revenue)) + "\n")
    output_file.write("Average Change: $" + str(ave_change) + "\n")
    output_file.write("Greatest Increase in Profits: " + str(max_increase_date) + " " +" " + "($"+ str(int(max_increase))+ ")" + "\n")
    output_file.write("Greatest Decrease in Profits: " + str(max_decrease_date) + " " +" " + "($"+ str(int(max_decrease))+ ")" + "\n")
    output_file.close()
