import os
import csv

# Path to collect data from the Resources folder

csvpath=os.path.join('.','Resources','election_data.csv')

# Variable Declaration
total_count=0
Candidate_list=[]
CTotal=[]
voter_id=[]

with open(csvpath,newline="")as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)

    #Loop through the data

    for row in csvreader:
        Candidate_list.append(row[2])
        voter_id.append(row[0])

# Calculate total votes, Percentage of vote by each candidate and winner
# Print the Result on terminal as well as write it on text file

output_path = os.path.join(".", "Output", "Result.txt")
with open(output_path, "w") as textfile: 

    # Total Voting done

    total_votes=len(voter_id)
    print("Election Results")
    textfile.write("Election Results\n")
    textfile.write("-----------------------\n")
    print("--------------------------")
    print("Total votes : ", len(voter_id))
    textfile.write("Total votes :{}\n".format(len(voter_id)))
    print("--------------------------")
    textfile.write("--------------------------\n")
    UnqCandidates = list(set(Candidate_list))
    ca_per={}

    # Total number and Percentage of votes by each candidate

    for i in range(len(UnqCandidates)):
        CTotal=Candidate_list.count(UnqCandidates[i])
        per=(CTotal/total_votes)*100
        X=round(per,6)
        print(f'{UnqCandidates[i]} : {X}% ({CTotal})')
        textfile.write("{0} : {1}% ({2})\n".format(UnqCandidates[i],X,CTotal))
        ca_per[UnqCandidates[i]]=X

    # Winner of the election
    
    maximum = max(ca_per, key=ca_per.get)
    textfile.write("---------------------\n")
    print("---------------------------")
    textfile.write("Winner :{}\n".format(maximum))
    print("Winner :",maximum)
    print("----------------------------")
    textfile.write("---------------------\n")
   
     

        
        

   


   

