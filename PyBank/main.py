# Import the os module
import os

# Module for reading CSV files
import csv

# Path to the csvfile
py_bank = os.path.join('Resources', 'budget_data.csv')

# Create lists to store data. 
monthly_changes = []

 # Initialize variables 
count = 0
changeCount = 0
totalProfit = 0
total_change_profits = 0
previousProfit = 0
monthly_change_profits = 0

greatest_inc_profits = 0
inc_date = ""
greatest_dec_profits = 0
dec_date = ""

# Open py_bank
with open(py_bank, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Read each row of data after header
    for row in csvreader:    
      # Count the number of months in dataset
      count = count + 1 

      currentProfit = int(row[1])
            
      # Calculate total profit
      totalProfit = totalProfit + currentProfit

      if previousProfit != 0:
        # Calculate average change in profits from month to month
        monthly_change_profits = currentProfit - previousProfit
        total_change_profits = total_change_profits + monthly_change_profits
        changeCount = changeCount + 1
        # print(f"change count in if = {changeCount}")
      
      previousProfit = currentProfit  
      
      if monthly_change_profits > greatest_inc_profits:
        greatest_inc_profits = monthly_change_profits
        inc_date = row[0]

      if monthly_change_profits < greatest_dec_profits:
        greatest_dec_profits = monthly_change_profits
        dec_date = row[0]  
    
      # Find maxiumum and minimum change in profits 
      # greatest_inc_profits = max(monthly_changes)
      # greatest_dec_profits = min(monthly_changes)

      # Find corresponding dates of when min and max change in profits occured
      # inc_date = date[monthly_changes.index(greatest_inc_profits)]
      # dec_date = date[monthly_changes.index(greatest_dec_profits)]

# Calculate average change in profit
# print(f"change count= {changeCount}")
# exit()
average_change_profits = total_change_profits/changeCount

output = f"""
Financial Analysis
----------------------------
Total Months: {count}
Total: ${totalProfit:,}
Average  Change: ${average_change_profits:,.2f}
Greatest Increase in Profits: {inc_date} (${greatest_inc_profits:,})
Greatest Decrease in Profits: {dec_date} (${greatest_dec_profits:,})
"""

print(output)

with open('financial_analysis.txt', 'w') as text:
   text.write(output)

# Print all values   
# print("----------------------------------------------------------")
# print("Financial Analysis")
# print("----------------------------------------------------------")
# print("Total Months: " + str(count))
# print("Total Profits: " + "$" + str(totalProfit))
# print("Average Change: " + "$" + str(int(average_change_profits)))
# print("Greatest Increase in Profits: " + str(inc_date) + " ($" + str(greatest_inc_profits) + ")")
# print("Greatest Decrease in Profits: " + str(dec_date) + " ($" + str(greatest_dec_profits)+ ")")
# print("----------------------------------------------------------")

    # Write output files
# with open('financial_analysis.txt', 'w') as text:
#     text.write("----------------------------------------------------------\n")
#     text.write("  Financial Analysis"+ "\n")
#     text.write("----------------------------------------------------------\n\n")
#     text.write("    Total Months: " + str(count) + "\n")
#     text.write("    Total Profits: " + "$" + str(totalProfit) +"\n")
#     text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
#     text.write("    Greatest Increase in Profits: " + str(inc_date) + " ($" + str(greatest_inc_profits) + ")\n")
#     text.write("    Greatest Decrease in Profits: " + str(dec_date) + " ($" + str(greatest_dec_profits) + ")\n")
#     text.write("----------------------------------------------------------\n")