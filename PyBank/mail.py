
import csv

count = 0
total = 0
ChangeList=[]
ProfitList=[]
DateList=[]
csvpath='C:\\DATA ANALYSTICS\\3-Homework-Python\\Phyton-Challenge-master\\PyBank\\Resources\\budget_data.csv'
Output_Path='C:\\DATA ANALYSTICS\\3-Homework-Python\\Phyton-Challenge-master\\PyBank\\Resources\\Financial_Analysis.txt'
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(csv_header)

    # Read each row of data after the header
    First_V= next(csvreader)
    previous= int(First_V[1])
    
    for row in csvreader:
        count = count + 1
        total = total + int(row[1])
        changes=int(row[1])-previous
        ChangeList.append(changes)
        previous=int(row[1])
        ProfitList.append(row[1])
        
                    
    
                           
        # print(row)
        # print(row[0])
        # print(row[1])
        
    High_Profit=max(ProfitList)
    Low_Profit=min(ProfitList)
   
   #  if row[1] == High_Profit 
   # print("Greatest Increase in Profits:"+str(row[0]) + str(row[1])
   # if row[1] == Low_Profit
   # print ("Greatest Decrease in Profits: " + str(row[0])+str(Low_Profit))
    
    
    # Financial Analysis
    print("Financial Analysis")
    print("---------------------------------")
    print("Total Months: " + str(count))
    print("Total: $" + str(total))
    print("Average Change:$" +str((sum(ChangeList)/len(ChangeList))))
    print("Greatest Increase in Profits: " + str(High_Profit))
    print("Greatest Decrease in Profits: " + str(Low_Profit))
    