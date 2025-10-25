Got it — you want a **clean, GitHub-ready Markdown** where the styling is consistent, sections are clearly separated, and code/commands render properly. Here’s a fully polished version:

````markdown
# 📊 Financial Data Exporter

[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)  
[![Alpha Vantage](https://img.shields.io/badge/Alpha%20Vantage-API-blueviolet)](https://www.alphavantage.co/support/#api-key)  

A Python script that fetches comprehensive financial data (Income Statement, Balance Sheet, and Cash Flow) for a publicly traded company using the **Alpha Vantage API**.  
It processes the data, calculates key metrics, and exports everything into a multi-tabbed, formatted Excel workbook with charts and a glossary.

---

## Table of Contents

1. [Features](#features)  
2. [Requirements](#requirements)  
3. [How to Run](#how-to-run)  
4. [Example Session](#example-session)  
5. [Output](#output)  
6. [License](#license)  

---

## Features

- **Comprehensive Data**  
  Pulls quarterly and annual data from Income Statement, Balance Sheet, and Cash Flow.  

- **Key Metrics**  
  Includes Revenue, Net Income, EPS, CFFO, Debt, and other important metrics automatically.  

- **TTM Calculations**  
  Calculates Trailing Twelve Month (TTM) values for Revenue, Net Income, and CFFO on the quarterly sheet.  

- **Multi-Sheet Excel Export**  
  Creates a single Excel file (`[TICKER]_financials.xlsx`) with four tabs:  
  1. **Quarterly Data** – All quarterly metrics, dates as columns.  
  2. **Annual Data** – All annual metrics, dates as columns (chronologically sorted).  
  3. **Charts** – Line charts for every annual metric.  
  4. **Definitions** – Glossary of financial metrics used.  

- **Smart Formatting**  
  Excel workbook includes:  
  - Frozen panes  
  - Number formats: Billions (B$), Percentages (0.0%), Currency ($0.00)  
  - Auto-fitted columns for readability  

---

## Requirements

- **Python 3**  
- **Libraries**: Install with pip:

```bash
pip install requests pandas openpyxl
````

* **Alpha Vantage API Key**
  Get a free key here: [Alpha Vantage](https://www.alphavantage.co/support/#api-key)

> **Note:** The free API key is limited to 25 calls/day. Each run makes 6 API calls (3 quarterly + 3 annual). Running too many times may hit the limit.

---

## How to Run

1. Save the script as `generator.py` (or another name) in a directory.
2. Open terminal/command prompt.
3. Navigate to the script directory:

```bash
cd path/to/your/script
```

4. Run the script:

```bash
python generator.py
```

5. Enter the prompted inputs:

   * **Ticker** (e.g., `AAPL`)
   * **Alpha Vantage API Key**

---

## Example Session

```bash
PS C:\your\folder> python generator.py
📊 Fetch quarterly and annual financials (Alpha Vantage)
Ticker (e.g. AAPL): MSFT
Alpha Vantage API key: YOUR_API_KEY_HERE
Fetching quarterly data...
Fetching annual data...
📈 Generating charts...
✅ Exported formatted Excel: MSFT_financials.xlsx
```

---

## Output

After running, the script generates an Excel file (e.g., `MSFT_financials.xlsx`) containing:

1. **Quarterly Data** – Formatted quarterly metrics (newest → oldest)
2. **Annual Data** – Formatted annual metrics (oldest → newest for charting)
3. **Charts** – Dashboard of line charts visualizing trends from "Annual Data"
4. **Definitions** – Glossary of financial metrics

---

## License

This project is licensed under the MIT License.



