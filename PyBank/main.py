#Importing the necessary modules/libraries
import os
import csv

#csv_file = os.path.join('folder_name', 'file.csv')
csvpath = os.path.join('Resources', 'budget_data.csv')

#define variables as integers
total_months = 0
total_profit_or_loss = 0
month_change_profit_or_loss = 0
prior_month_change_profit_or_loss = 0
first_month_profit_or_loss = 0
last_month_profit_or_loss = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ''
greatest_decrease_month = ''

#Opening and reading the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Reading the header row
    csv_header = next(csvreader)

    #Reading the first row (that we tract the changes properly)
    #Variable to hold first_months_Profit_or_loss
    first_months_profit_or_loss = 0
    last_months_profit_or_loss = 0

    for row in csvreader:
        total_months += 1
        total_profit_or_loss +=int(row[1])
        if total_months == 1:
            first_months_profit_or_loss = int(row[1])
        else:
            last_months_profit_or_loss = int(row[1])
        
        if total_months > 1:
            month_change_profit_or_loss = int(row[1]) - prior_month_change_profit_or_loss

        prior_month_change_profit_or_loss = int(row[1])

        #Total_months to be one less : 86 - 1 = 85
        

        if month_change_profit_or_loss > greatest_increase:
            greatest_increase = month_change_profit_or_loss
            greatest_increase_month = row[0]

        if month_change_profit_or_loss < greatest_decrease:
            greatest_decrease = month_change_profit_or_loss
            greatest_decrease_month = row[0]

    average_change = (last_months_profit_or_loss - first_months_profit_or_loss) /(total_months - 1)

#Displaying information
print('Financial Analysis')
print('---------------------------')
print('Total Months: ' +str(total_months))
print('Total: $' + str(total_profit_or_loss))
print('Average Change: $' + str(round(average_change,2)))
print('Greatest Increase in Profits: ' + greatest_increase_month + ' ($' + str(greatest_increase) +')')
print('Greatest Decrease in Profits: ' + (greatest_decrease_month) + ' ($' + str(greatest_decrease) + ')')

output = open('analysis.txt', 'w')

line1 = 'Financial Analysis'
line2 = '--------------------------'
line3 = str(f'Total Months: {str(total_months)}')
line4 = str(f'Total: ${str(total_profit_or_loss)}')
line5 = str(f'Average Change: ${str(round(average_change,2))}')
line6 = str(f'Greatest Increase in Profits: {greatest_increase_month} (${str(greatest_increase)}') 
line7 = str(f'Greatest Decrease in Profits: {greatest_decrease_month} (${str(greatest_decrease)}')
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2,line3,line4,line5,line6,line7))