#import modules
import os
import csv
#create trackers
months_total = 0
revenue_total = 0
past_revenue = 0
highest_increase = 0
lowest_decrease = 99999999999
#create lists to store revenue change
revChange = []
#create path
budget_csvpath = "budget_data.csv"
#print(budget_csvpath)
#read csv file
with open(budget_csvpath, newline='', encoding='utf-8') as csvfile:
    budget_csvreader = csv.reader(csvfile, delimiter=',')
    #print(budget_csvreader)
    next(budget_csvreader, None)
    for row in budget_csvreader:
        #count total months in csv file
        months_total = months_total + 1
        #print(type(row[1])) <--used to figure out if working with str or int
        #count total revenue in csv file
        totalRev = revenue_total + (int(row[1]))
        #create a variable that will count the revenue change
        monthlyRevChange = int(row[1]) - past_revenue
        past_revenue = int(row[1])
        #add changes in new list
        revChange.append(monthlyRevChange)
        #calculate the average change in revenue
        avgRevChange = round(sum(revChange)/months_total)
        #print(avgRevChange)
        #find the greatest increase in revenue
        if (monthlyRevChange > highest_increase):
            highestIncMonth = row[0]
            highest_increase = monthlyRevChange
        #find the greatest decrease in revenue
        if (monthlyRevChange < lowest_decrease):
            lowestDecMonth = row[0]
            lowest_decrease = monthlyRevChange

#create varible to hold finanical analysis results and use f-strings for formatting
Results = (
f"Financial Analysis \n"
f"---------------------------- \n"
f"Total Months: {months_total} \n"
f"Total Revenue: ${revenue_total} \n"
f"Average Revenue Change: ${avgRevChange} \n"
f"Greatest Increase in Revenue: {highestIncMonth} (${highest_increase}) \n"
f"Greatest Decrease in Revenue: {lowestDecMonth} (${lowest_decrease}) \n")
print(Results)

#write a text file in order to export results to text file
outputtxt = os.path.join("PyBank_results.txt")
with open(outputtxt, 'w') as txtfile:
    txtwriter = txtfile.write(Results)