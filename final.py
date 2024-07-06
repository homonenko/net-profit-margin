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

#Artem
except PermissionError:
        print(f"Permission denied: '{path}'. Please check the file permissions.")
        return None
    except FileNotFoundError:
        print(f"File not found: '{path}'. Please check the file path.")
        return None

def process_data(data):
        if data:
            header_info = ' | '.join(data[0])
            total_records = len(data) - 1
            return header_info, total_records
    else:
        return "", 0

while True:
    print("1. Display existing information")
    print("2. Add a new data source (file)")
    print("3. Compute metric")

