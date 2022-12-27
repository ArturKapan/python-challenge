# importing moduls for csv file
import os
import csv

# defining variables
total_months = 0
net_total_amount = 0
greatest_increase = 0
greatest_decrease = 0
current_change = 0
months = []
monthly_loss_profit_changes = []
    

#creating csv file path
file_path='Resources/budget_data.csv'


# open csv file and read
with open(file_path, "r") as csv_file:
    csv_read=csv.reader(csv_file, delimiter=",")


    # seperating the headers
    csv_header=next(csv_read)
    
    
    
   # looping through the csv file
    for row in csv_read:
        
        
       # The total number of months included in the dataset
        total_months = total_months+1

       # The net total amount of "Profit/Losses" over the entire period 
        net_total_amount += int(row[1])

        # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        current_month = int(row[1])

        # for first row, there is not previus month
        if total_months == 1:
            previus_month = current_month 
            continue
        # for rest of rows
        else:
            current_change = current_month - previus_month
            
            monthly_loss_profit_changes.append(current_change)
            months.append(row[0])
            previus_month = current_month

    # average of all changes        
    ave_changes = round( sum(monthly_loss_profit_changes)/len(monthly_loss_profit_changes), 2)

    # The greatest increase in profits (date and amount) over the entire period

    greatest_increase = max(monthly_loss_profit_changes)
    best_month = months[monthly_loss_profit_changes.index(greatest_increase)]
    
    # The greatest decrease in profits (date and amount) over the entire period

    greatest_decrease = min(monthly_loss_profit_changes)
    the_worse_month = months[monthly_loss_profit_changes.index(greatest_decrease)]


print(f''' ``` Text 
Financial Analysis
________________________________
Total Months: {total_months}
Total:  ${net_total_amount}  
Average Change:${ave_changes} 
Greatest Increase in Profits: {best_month} (${greatest_increase} )
Greatest Decrease in Profits: {the_worse_month} (${greatest_decrease})
````''')
    

    