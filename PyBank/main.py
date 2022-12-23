# importing moduls for csv file
import os
import csv

#creating csv file path
file_path='../PyBank/Resources/budget_data.csv'

# open csv file and read
with open(file_path, "r") as read:
    csv_read=csv.reader(read, delimiter=",")

     # seperating the headers
    csv_header=next(csv_read)
    # print(f"header {csv_header}")
    # # printing csv file row by row
    # for row in csv_read:
    #     print(row)

 # The total number of months included in the dataset  
    total_months=0

    for row in csv_read:
        total_months=total_months+1
    print(total_months)    
        
   
    
# The net total amount of "Profit/Losses" over the entire period




# The changes in "Profit/Losses" over the entire period, and then the average of those changes




# The greatest increase in profits (date and amount) over the entire period





# The greatest decrease in profits (date and amount) over the entire period



    