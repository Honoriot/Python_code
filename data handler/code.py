import csv

Name = input("Name: ")
Age = int(input("Age: "))
DOB = input("DOB(date-month-year): ")

with open("Filename.csv", mode='w') as csv_file:
    field = [Name, Age, DOB]
    writer = csv.DictWriter(csv_file, fieldnames = field)

    