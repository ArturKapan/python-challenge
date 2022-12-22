
import os
import csv

budget_data = os.path.join("..", "PyBank","Resources", "budget_data.csv")

with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    for row in csv_reader:
        print(row)  
     

    