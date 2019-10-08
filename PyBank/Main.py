import os
import csv

# Path to collect data from the Resources folder

csvpath=os.path.join('.','Resources','budget_data.csv')

#Variable Declaration

count=0
Total=0.0
Average=0.0
greatest_Increase=0.0
greatest_Decrease=0.0

#Print the Financial Analysis result to the terminal

def print_Stats():
    print("Financial Analyssis")
    print("---------------------------------")
    print(f'Total Months:{count}')
    print(f'Total:${Total}')
    print(f'Average Change:${Total/count}')
    print(f'Greatest Increase in Profits:{date_Increase} (${greatest_Increase})')
    print(f'Greatest Decrease in Profits:{date_Decrease} (${greatest_Decrease})')

#Read in the csv file

with open(csvpath,newline="")as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)

    #Loop through the data

    for row in csvreader:

        # Find the total number of months
        count+=1

        # Find the total Amount of Profit/Loss
        Total=Total+(float(row[1]))

        # Find the Greatest Increase and Greatest Decrease with (Date and Amount)
        if (float(row[1]))>greatest_Increase:
            greatest_Increase=(float(row[1]))
            date_Increase=(row[0])
        elif (float(row[1]))<greatest_Decrease:
            greatest_Decrease=(float(row[1]))
            date_Decrease=(row[0])

# Run the print_status() function to print the Financial Analysis Result

print_Stats()

# Specify the file to write to
output_path = os.path.join(".", "Output", "Result.txt")
with open(output_path, "w") as textfile:
    textfile.write("Financial Analyssis\n")
    textfile.write("--------------------------------\n")
    textfile.write("Total Months:{}\n".format(count))
    textfile.write("Total:{}\n".format(Total))
    textfile.write("Average Change: {}\n".format(Total/count))
    textfile.write("Greatest Increase in Profits:{0} (${1})\n".format(date_Increase,greatest_Increase))
    textfile.write("Greatest Decrease in Profits:{0} (${1})\n".format(date_Decrease,greatest_Decrease))
    
    textfile.close()


      
    

