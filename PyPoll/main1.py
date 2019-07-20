import csv
Total_Votes=0
CandidateList=[]
Candidate_Votes={}

csvpath = 'C:\\DATA ANALYSTICS\\3-Homework-Python\\Phyton-Challenge-master\\PyPoll\\Resources\\election_data.csv'
output_path = "C:\DATA ANALYSTICS\\3-Homework-Python\\Phyton-Challenge-master\\PyBank\\Resources\Election_Votes.txt"

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        Total_Votes=Total_Votes+1
        Candidate=row[2]
        # Adding candidate not in the list already
        if Candidate not in CandidateList:
            CandidateList.append(Candidate)
            Candidate_Votes[Candidate]=0
            
        Candidate_Votes[Candidate] = Candidate_Votes[Candidate]+1
        
    for Candidate in Candidate_Votes:
        Votes=Candidate_Votes[Candidate]
        Percentage=round(float(Votes) / float(Total_Votes),3)*100
        print(str(Candidate)+":"+ str(Percentage)+"%"+"("+str(Votes)+")")
        
    print("Election Results")
    print("-----------------")
    print("Total Votes :"+ str(Total_Votes))
    print("--------------------")
   
   
       
       
       
    
    
    
    
        
          
    
   
          


    
   

    
    
    




    
    


    


    


