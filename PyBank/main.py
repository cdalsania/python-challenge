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
total_month_change = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ''
greatest_decrease_month = ''