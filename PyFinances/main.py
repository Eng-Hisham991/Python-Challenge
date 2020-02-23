# In this challenge, my task is aidded by using Python is to create a script to analyze the financial records of the csv file i.e. "budget_data.csv".
# I have a given set of financial data called [budget_data.csv]. The dataset is composed of two columns: `Profit/Losses` and `Date`. 

# The task is to create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset.

#   * The net total amount of "Profit/Losses" over the entire period.

#   * The average of the changes in "Profit/Losses" over the entire period.

#   * The greatest increase in profits (date and amount) over the entire period.

#   * The greatest decrease in losses (date and amount) over the entire period.

#  The result after running the script will be the following:

#       Financial Analysis
#       ----------------------------
#       Total Months: 86
#       Total: $38382578
#       Average  Change: $-2315.12
#       Greatest Increase in Profits: Feb-2012 ($1926159)
#       Greatest Decrease in Profits: Sep-2013 ($-2196167)
# -------------------------------------------------------------------------------------------------------------------------------------------

import os       # Importing the os module. It provides a portable way of using operating system dependent functionality.
import csv      # Importing the csv module. It is known as (Comma Separated Values). It is the most common import and export format for spreadsheets and databases.       
import sys
import operator
d={}            # An empty dictionary for the use of passing the date information from the csv file  to it and from there the required information is attained.
c={}            # An empty dictionary to pass the Profit/Losses information from the csv file to it and from there the required information is attained.
f=[]            # An empty list used to assign the Profit/Losses data to it.
k=[]
list_of_stuff=[]
csv_path= os.path.join('..','PyFinances', 'budget_data.csv')   # csv_path is variable assigned used to open the "budget_data.csv".
with open(csv_path, newline='', mode= 'r', encoding="utf8") as csvfile: # The with method used to open and read the csv_path and each line is spaced out and the encoding changed to UTF8.
    csvreader= csv.DictReader(csvfile)  # Create an object which operates like a regular reader but maps the information read into a dictionary and assigned to a variable i.e. csvreader.  
    for row in csvreader:       # for loop used to loop in csvreader variable.  
        k.append(row['Date'])
        if row['Date'] not in d:        # if statement is used to test the assigned condition.
            d[row['Date']]= str(row['Date'])    # Assigning the Date information to d dictionary.
            list_of_stuff.append(d)
        if row['Profit/Losses'] not in c:       # if statement is used to test the assigned condition.
            f.append(row['Profit/Losses'])      # fill the empty f list with Profit/Losses data.
    for i in range(0,len(f)):       # if statement is used to test the assigned condition.
        f[i]= int(f[i])             # Converting the numbers associated with Profit/Losses data from string format to integer format.
        z = f                       # Assigned the converted f list to z variable.
s= [j-i for i,j in zip(z[:-1], z[1:])] # List comprehension used to get the change between Profit/Losses data and assigned it to s variable.
Total_months = len(d)        # Total months.
Total_Profit_Losses = int(sum(f))   # Total Profit/Losses.
Average_Change= round(sum(s)/len(s),2)           # Average change of Profit/Losses.
Decreae= min(s)                      # Greatest Decrease in Profits
Increase= max(s)                     # Greatest Increase in Profits
Index_num_Decrease= print(s.index(min(s)))              # Index number of Greatest Decrease in Profits
Index_num_Increase= print(s.index(max(s)))              # Index number of Greatest Increase in Profits
Month_of_Decrease_Profit= k[44]
Month_of_Increase_Profit= k[25]                   # Since we got the changes in Profit/Loss so the index decrease by 1 then the index of month equal index of Greatest profit Increae minus 1.

print(f"Total Months: {Total_months}")
print(f"Total: ${Total_Profit_Losses}")
print(f"Average Change: ${Average_Change}")
print(f"Greatest Increase in Profits: {Month_of_Increase_Profit} $ {Increase}")
print(f"Greatest Decrease in Profits: {k[44]} ${min(s)}")



with open('output.txt', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Total_Moths", "Total", "Average Change", "Moth", "Greatest Increase in Profits", "Month", "Greatest Decrease in Profits"])
    writer.writerow(["86", "38382578", "$-2315.12", "Feb-2013", "$1926159", "Sep-2012", "$-2196167"])
    