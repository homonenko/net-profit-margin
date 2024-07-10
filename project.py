import csv
import os

data_sources = []

def compute_metric():
    if not data_sources:
        print("No data sources available.")
        return

    print("Select a data source:")
    for index, (path, _) in enumerate(data_sources, start=1):
        print(f"{index}. {os.path.basename(path)}")
    try:
        choice = int(input("Enter the number of the data source: ").strip())
        if 1 <= choice <= len(data_sources):
            path = data_sources[choice - 1][0]
            data = read_csv(path)
            if data:
                header_info, total_records = process_data(data)
                print(f"Selected data source: {os.path.basename(path)} | Total records: {total_records}")
                net_profit_margin = compute_net_profit_margin(data)
                print(f"Net Profit Margin: {net_profit_margin:.2f}%")
                data_sources[choice - 1] = (path, f"Net Profit Margin = {net_profit_margin:.2f}%")
            else:
                print("Failed to read the data source.")
        else:
            print("Invalid choice. Try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except FileNotFoundError:
        print("File not found.")

def compute_net_profit_margin(data):
    try:
        total_revenue = sum(float(row[8]) for row in data[1:])
        net_income = sum(float(row[30]) for row in data[1:])
        return (net_income / total_revenue) * 100 if total_revenue else 0
    except ValueError:
        print("Error in data format.")
        return 0

def read_csv(path):
    try:
        with open(path.strip(), 'r') as file:
            csv_reader = csv.reader(file)
            data = [row for row in csv_reader]
        return data
    except PermissionError:
        print(f"Error for '{path}'.")
        return None
    except FileNotFoundError:
        print(f"Error for '{path}'.")
        return None

def process_data(data):
    if data:
        header_info = ' | '.join(data[0])
        total_records = len(data) - 1
        return header_info, total_records
    else:
        return "", 0

def display_existing_info():
    if not data_sources:
        print("No data sources available.")
    else:
        for index, (path, metric) in enumerate(data_sources[-3:], start=1):
            print(f"{index}) Data source: {os.path.basename(path)} | Metric: {metric}")

while True:
    print("1. Display existing information")
    print("2. Add a new data source (file)")
    print("3. Compute metric")
    print("4. Exit")
    user_choice = input("Enter your choice: ").strip()
    if user_choice == "1":
        display_existing_info()
    elif user_choice == "2":
        file_path = input("Enter file path: ").strip()
        data = read_csv(file_path)
        if data:
            header_info, total_records = process_data(data)
            data_sources.append((file_path, "Metric not calculated"))
            print(f'Headers: {header_info}\nTotal records: {total_records}')
    elif user_choice == "3":
        compute_metric()
    elif user_choice == "4":
        break
    else:
        print("Invalid choice. Try again")

#моментами помагав гпт

