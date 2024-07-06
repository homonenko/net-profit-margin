import csv
import os


data_sources = []

def display_existing_info():
    if not data_sources:
        print("No data sources available.")
    else:
        for index, (path, metric) in enumerate(data_sources[-3:], start=1):
            print(f"{index}) Data source: {os.path.basename(path)} | Metric: {metric}")

def compute_metric():
    if not data_sources:
        print("No data sources available.")
        return

    print("Select a data source:")
    for index, (path, _) in enumerate(data_sources, start=1):
        print(f"{index}. {os.path.basename(path)}")
    try:
        selection = int(input("Enter the number of the data source: ").strip())
        if 1 <= selection <= len(data_sources):
            path = data_sources[selection - 1][0]
            data = read_csv(path)


