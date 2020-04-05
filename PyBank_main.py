#Budget Data CVS Script
#Only 2 colums: Date and Profit/Losses
#total number of months
#net total maount of profit & losses
#average fo the changes in p & f
#greatest incerase in profits (date and amount)
#greatest decrese as well

import os
import csv

budgets = budget_data.csv

dates, revenue = ([]for i in range (2))
csv_path = os.path.join("budget_data", budgets)
summary_txt = budget_summary.summary_txt




with open(csv_path, mode = 'r', newline='') as budget_data
    reader = csv.reader(budget_data, delimeter=',')

next(reader)

row_number = 0
for row in reader:
    date.append(row[0])
    revenue.append(row[1])
    row_number = +1

print('Financial Analysis -' *50)
print('----------------------------')
#total number of months

print('Total Months', row_numbers)

#net total amount of profits & losses

sum_of_revenue = 0
    for i in revenue:
        sum_of_revenue += int(i)
print('Total Revenue: $'+str(sum_of_revenue))

#average of changes in profits & losses

total_changes = 0
for h in range(row_number):
    total_changes += int(revenue[h] - int(revenue[h-1]))
print("Average Revenue Change: $" +str(round(total_changes)))

#increase in revenue
highest_revenue = 0
for j in range(len(revenue)):
    if int(revenue[j]) - int(revenue[j-1]) > highest_revenue:
        highest_revenue = int(revenue[j]) - int(revenue[j-1])
        highest_month = date[j]

print('Greatest Increase in Revenue:',highest_month, ('$' + str(highest_revenue + '')

#decrease part

lowest_revenue = 0
for k in range(len(revenue)):
    if int(revenue[k])-int(revenue[k-1]) < lowest_revenue:
        lowest_revenue = int(revenue[k])-int(revenue[k-1])
        lowest_month = date[k]

print('Greatest Decrease in Revenue:', lowest_month, ('$' + str(lowest_revenue)+ ''))

#txt file

writer = csv.writer(summary_txt)
writer.writerow([
    ["Financial Analysis for:" + csv_path],
    ['-' * 50]
    ['Total Months:' + str(row_number)],
    ['Total Revenue: $'] + str(sum_of_revenue)],
    ['Average Revenue Change: $' + str(round(total_changes))],
    ['Greatest Increase in Revenue: ' + str(highest_month) + ("$" + str(highest_revenue)+'')]
    ['Greatest Decrease in Revenue: ' + str(lowest_month) + ('$' + str(lowest_revenue)+ '')]

])


