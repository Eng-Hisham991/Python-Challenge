
import os
import csv
import operator
from collections import Counter
C={}
csv_path= os.path.join('..', 'PyElections', 'houston_election_data.csv')
with open(csv_path, newline='', mode= 'r', encoding="utf8") as csvfile:
    csvreader= csv.DictReader(csvfile)
    for row in csvreader:
        if row['Candidate'] not in C:
            C[row['Candidate']]= 1
        else:
            C[row['Candidate']]+=1
Total_Vote= sum(C.values())
print("Total number of votes cast : ", Total_Vote)
Sorted_C = sorted(C.items(), key=operator.itemgetter(1),reverse=True)
for count in Sorted_C:
    AA= print(f" {count[0]} : {round (100*(count[1]/Total_Vote),2 )} % {count[1]}")

print(f"Total Cast Votes: {Total_Vote}")


with open('output.txt', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Total Cast Votes", "Sylvester Turner", "Tony Buzbee", "Bill King %", "111789"])
    writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
    writer.writerow([3, "Guido van Rossum", "Python Programming"])
#   Sylvester Turner: 46.38% (111789)
#   Tony Buzbee: 28.78% (69361)
#   Bill King: 14.01% (33772)
#   Dwight A. Boykins: 5.90% (14212)
#   Victoria Romero: 1.22% (2933)
#   Sue Lovell: 1.22% (2932)
#   Demetria Smith: 0.70% (1694)
#   Roy J. Vasquez: 0.65% (1556)
#   Kendall Baker: 0.41% (982)
#   Derrick Broze: 0.28% (686)
#   Naoufal Houjami: 0.23% (560)
#   Johnny “J.T.” Taylor: 0.23% (555)
#   -----------------------------------------
#   1st Advancing Candidate: Sylvester Turner
#   2nd Advancing Candidate: Tony Buzbee
#   -----------------------------------------