import csv
import os


while True:
    print("1. Check existing information")
    print("2. Add a new data source(file)")
    print("3. Calculate metric")
    print("4. Exit")
    choice = input("Enter your choice: ").strip()
    if choice == "1":

    elif choice == "2":
        file_path = input("Enter file path: ").strip()
        data = read_csv(file_path)

    elif choice == "3":

    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again")


def read_csv(path):
        with open(path.strip(),'r') as file:
            csv_reader = csv.reader(file)
            data = [row for row in csv_reader]
        return data
