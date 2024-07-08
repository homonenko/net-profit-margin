# net-profit-margin
# This program allows users to manage and compute metrics for data sources stored in CSV files. It includes features to display existing data sources, add new data sources, and compute specific metrics (e.g., Net Profit Margin) based on the data
# it can 
 1. Display Existing Information
 2. Add a New Data Source
 3. Compute Metric
 4. Exit
# Functions and descrtiption 
'display_existing_info()'

Displays the last three data sources and their metrics if available, otherwise informs the user that no data sources are available.

'compute_metric()'

Allows the user to select a data source and computes the Net Profit Margin based on the CSV data. Updates the data source list with the computed metric.

'compute_net_profit_margin(data)'

Calculates the Net Profit Margin using the total revenue and net income columns from the CSV data.

'read_csv(path)'

Reads the CSV file from the given path and returns the data as a list of rows. Handles errors such as file not found and permission issues.

'process_data(data)

Processes the CSV data to extract header information and the total number of records.
```
1. Display existing information
2. Add a new data source (file)
3. Compute metric
4. Exit
Enter your choice: 1


```
# Output 
```
1) Data source: AAPL.csv | Metric: Metric not calculated
2) Data source: GOOG.csv | Metric: Net Profit Margin = 19.12%
3) Data source: NFLX.csv | Metric: Metric not calculated

```


