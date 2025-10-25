# 📊 Financial Data Exporter

[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)  
[![Alpha Vantage](https://img.shields.io/badge/Alpha%20Vantage-API-blueviolet)](https://www.alphavantage.co/support/#api-key)  

A Python script that fetches comprehensive financial data (Income Statement, Balance Sheet, and Cash Flow) for a publicly traded company using the **Alpha Vantage API**. It processes the data, calculates key metrics, and exports everything into a multi-tabbed, formatted Excel workbook with data visualizations.

---

## Table of Contents

- [Features](#features)  
- [Requirements](#requirements)  
- [How to Run](#how-to-run)  
- [Example Session](#example-session)  
- [Output](#output)  

---

## Features

- **Comprehensive Data**: Pulls quarterly and annual data from Income Statement, Balance Sheet, and Cash Flow statements.  
- **Key Metrics**: Automatically includes metrics like Revenue, Net Income, EPS, CFFO, Debt, etc.  
- **TTM Calculations**: Calculates Trailing Twelve Month (TTM) figures for Revenue, Net Income, and CFFO on the quarterly data sheet.  
- **Multi-Sheet Excel Export**: Generates a single Excel file (`[TICKER]_financials.xlsx`) with four tabs:  
  1. **Quarterly Data** – All quarterly financial metrics, dates as columns.  
  2. **Annual Data** – All annual financial metrics, dates as columns (chronologically sorted).  
  3. **Charts** – Line charts for every annual metric.  
  4. **Definitions** – Glossary of financial metrics.  
- **Smart Formatting**: Excel workbook includes:  
  - Frozen panes for easy scrolling  
  - Specific number formats (Billions (B$), Percentages 0.0%, Currency $0.00)  
  - Auto-fitted column widths  

---

## Requirements

- **Python 3**  
- **Python Libraries**: Install required libraries:

```bash
pip install requests pandas openpyxl
Alpha Vantage API Key: Get a free key here.

Note: The free key is limited (25 calls per day). Each run uses 6 API calls (3 quarterly + 3 annual). Exceeding this limit will stop the script until the next day.

How to Run
Save the script as generator.py (or any preferred name) in a directory.

Open terminal/command prompt.

Navigate to the script directory:

bash
Copy code
cd path/to/your/script
Run the script:

bash
Copy code
python generator.py
Enter the prompted inputs:

Ticker (e.g., AAPL)

Alpha Vantage API Key

Example Session
bash
Copy code
PS C:\your\folder> python generator.py
📊 Fetch quarterly and annual financials (Alpha Vantage)
Ticker (e.g. AAPL): MSFT
Alpha Vantage API key: YOUR_API_KEY_HERE
Fetching quarterly data...
Fetching annual data...
📈 Generating charts...
✅ Exported formatted Excel: MSFT_financials.xlsx
Output
After running, the script generates a formatted Excel file (e.g., MSFT_financials.xlsx) with these tabs:

Quarterly Data – Formatted quarterly metrics (newest to oldest).

Annual Data – Formatted annual metrics (oldest to newest for proper charting).

Charts – Dashboard of line charts visualizing trends from "Annual Data".

Definitions – Glossary of all financial metrics.

License
This project is licensed under the MIT License.