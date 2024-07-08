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
# 1. Display existing information

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

# 2. Add a new data source (file)
```
1. Display existing information
2. Add a new data source (file)
3. Compute metric
4. Exit
Enter your choice: 2
```
# Output
```
Enter file path: RDDT.csv
Headers: ﻿date |  symbol |  reportedCurrency |  cik |  fillingDate |  acceptedDate |  calendarYear |  period |  revenue |  costOfRevenue |  grossProfit |  grossProfitRatio |  researchAndDevelopmentExpenses |  generalAndAdministrativeExpenses |  sellingAndMarketingExpenses |  sellingGeneralAndAdministrativeExpenses |  otherExpenses |  operatingExpenses |  costAndExpenses |  interestIncome |  interestExpense |  depreciationAndAmortization |  ebitda |  ebitdaratio |  operatingIncome |  operatingIncomeRatio |  totalOtherIncomeExpensesNet |  incomeBeforeTax |  incomeBeforeTaxRatio |  incomeTaxExpense |  netIncome |  netIncomeRatio |  eps |  epsdiluted |  weightedAverageShsOut |  weightedAverageShsOutDil |  link |  finalLink |  lastRetainedEarnings |  stockRepurchases |  dividendsPaid |  otherDistributions |  retainedEarnings |  grossPPE |  annualDepreciation |  capitalExpenditure |  netPPE |  lastGoodwill |  acquisitionsAndAdjustments |  goodwill
Total records: 4
```
# 3. Compute metric
```
1. Display existing information
2. Add a new data source (file)
3. Compute metric
4. Exit
Enter your choice: 3
```
# Output
```
Select a data source:
1. AAPL.csv
2. GOOG.csv
3. NFLX.csv
4. RDDT.csv
Enter the number of the data source: 3
Selected data source: NFLX.csv | Total records: 4
Net Profit Margin: 11.09%
```
# Menu Choice Validation

Ensures that the user inputs a valid menu choice (1-4).
```
Enter your choice: 5
Invalid choice. Try again.
```
# File Path Validation

Checks if the file exists and has the correct permissions.
```
Enter file path: invalid/path.csv
File not found: 'invalid/path.csv'. Please check the file path.
```
# CSV Data Validation

Ensures that the CSV data contains valid numeric values for revenue and net income.

```
Error in data format. Please ensure the CSV contains valid numeric values for revenue and net income.
```
# Empty Input File

Handles cases where the input file is empty gracefully.

```
Enter file path: empty.csv
Headers: 
Total records: 0
```
# Large Input File

Performance tested with a large input file (e.g., 5 MB).
```
25 seconds to process a large file.
```
# Maks
Functional Menu: Maks developed the main interactive menu that allows users to navigate through the program's functionalities. This menu provides options to display existing information, add new data sources, compute metrics, and exit the program.
Function display_existing_info(): Maks implemented this function to display the last three data sources and their calculated metrics, if available. This function ensures that users can quickly view recent data sources and their associated metrics.
Function read_csv(): Maks also wrote the function responsible for reading CSV files. This function handles file reading, ensuring that data is correctly loaded into the program, and manages potential errors such as file not found or permission issues.
# Vlada
Function compute_metric(): Vlada developed this function to calculate the metrics for the selected data source. This involves prompting the user to select a data source and then computing the Net Profit Margin based on the data within the CSV file.
Function compute_net_profit_margin(): Vlada also wrote this function, which calculates the Net Profit Margin using the total revenue and net income columns from the CSV data. This function ensures accurate financial calculations and handles potential data format errors.
# Artem
Function process_data(): Artem was responsible for creating this function, which processes the CSV data to extract header information and calculate the total number of records. This function is crucial for providing users with an overview of the data contained within the CSV file.
