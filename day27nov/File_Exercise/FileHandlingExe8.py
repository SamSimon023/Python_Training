#read a CSV file named students.csv and print name and marks of each student.

import csv
 
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"Name: {row[0]}, Marks: {row[1]}")
