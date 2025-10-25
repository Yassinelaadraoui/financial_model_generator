Financial Data Exporter
This is a Python script that fetches comprehensive financial data (Income Statement, Balance Sheet, and Cash Flow) for a publicly traded company using the Alpha Vantage API. It processes the data, calculates key metrics, and exports everything into a multi-tabbed, formatted Excel workbook, complete with data visualizations.

Features
Comprehensive Data: Pulls quarterly and annual data from the Income Statement, Balance Sheet, and Cash Flow statements.

Key Metrics: Automatically maps and includes key metrics like Revenue, Net Income, EPS, CFFO, Debt, etc.

TTM Calculations: Automatically calculates Trailing Twelve Month (TTM) figures for Revenue, Net Income, and CFFO on the quarterly data sheet.

Multi-Sheet Excel Export: Generates a single, clean Excel file ([TICKER]_financials.xlsx) with four distinct tabs:

Quarterly Data: All quarterly financial metrics, with dates as columns.

Annual Data: All annual financial metrics, with dates as columns (sorted chronologically).

Charts: A dedicated sheet with line charts for every annual metric, making it easy to visualize trends.

Definitions: A simple glossary defining all the financial metrics used in the report.

Smart Formatting: The Excel file is professionally formatted with:

Frozen panes for easy scrolling.

Specific number formats (Billions (B$), Percentages 0.0%, Currency $0.00).

Auto-fitted column widths for readability.

Requirements
To run this script, you will need:

Python 3: Ensure you have Python 3 installed.

Python Libraries: You must install the required libraries. You can install them using pip:

Bash

pip install requests pandas openpyxl
Alpha Vantage API Key: This script requires a free API key from Alpha Vantage.

You can get your free key here: https://www.alphavantage.co/support/#api-key

Note: The free key is highly limited (e.g., 25 calls per day). This script makes 6 API calls (3 for quarterly, 3 for annual) every time it runs. If you run it too many times, you will hit your limit and it will stop working until the next day.

How to Run
Save the code as generator.py (or any name you prefer) in a directory.

Open your terminal or command prompt.

Navigate to the directory where you saved the script.

Bash

cd path/to/your/script
Run the script using python:

Bash

python generator.py
The script will prompt you for two inputs:

Ticker (e.g. AAPL): Enter the stock ticker for the company you want to analyze (e.g., AAPL, MSFT, TEAM).

Alpha Vantage API key: Paste your API key.

Example Session
Bash

PS C:\your\folder> python generator.py
📊 Fetch quarterly and annual financials (Alpha Vantage)
Ticker (e.g. AAPL): MSFT
Alpha Vantage API key: YOUR_API_KEY_HERE
Fetching quarterly data...
Fetching annual data...
📈 Generating charts...
✅ Exported formatted Excel: MSFT_financials.xlsx
Output
After running, you will find a new Excel file in the same directory (e.g., MSFT_financials.xlsx).

This file will contain the following tabs:

Quarterly Data: Formatted quarterly metrics, newest to oldest.

Annual Data: Formatted annual metrics, oldest to newest (to ensure charts work correctly).

Charts: A full dashboard of line charts visualizing the trend of every metric from the "Annual Data" sheet.

Definitions: A helpful glossary.