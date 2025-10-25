"""
data_builder.py

Contains all logic for fetching and processing financial data
into pandas DataFrames. All calculations, ratios, and
transformations happen here.
"""

import pandas as pd
from api import fetch_alpha_vantage_data
from utils import safe_convert_to_float

def fetch_summary_data(ticker: str, api_key: str) -> pd.DataFrame:
    """
    Fetches key valuation and overview metrics from the OVERVIEW endpoint.
    """
    print(f"Fetching summary/valuation data for {ticker}...")
    json_data = fetch_alpha_vantage_data("OVERVIEW", ticker, api_key)
    
    metrics_to_pull = [
        "MarketCapitalization", "EBITDA", "PERatio", "PEGRatio", 
        "PriceToBookRatio", "DividendYield", "PayoutRatio", "EVToEBITDA",
        "BookValue", "52WeekHigh", "52WeekLow", "AnalystTargetPrice"
    ]
    
    summary_data = {}
    for metric in metrics_to_pull:
        summary_data[metric] = json_data.get(metric, 'N/A')
        
    for metric in ["MarketCapitalization", "EBITDA", "AnalystTargetPrice"]:
        summary_data[metric] = safe_convert_to_float(json_data, metric)
        
    for metric in ["PERatio", "PEGRatio", "PriceToBookRatio", "DividendYield", "PayoutRatio", "EVToEBITDA"]:
         summary_data[metric] = safe_convert_to_float(json_data, metric)

    df = pd.DataFrame.from_dict(summary_data, orient='index', columns=['Value'])
    df.index.name = "Metric"
    return df


def build_financials_dataframe(ticker: str, api_key: str, period: str) -> pd.DataFrame:
    """
    Generic function to fetch, combine, and transform financial data
    for either 'quarterly' or 'annual' periods.
    """
    report_key = f"{period}Reports"
    
    income_data = fetch_alpha_vantage_data("INCOME_STATEMENT", ticker, api_key)
    balance_sheet_data = fetch_alpha_vantage_data("BALANCE_SHEET", ticker, api_key)
    cash_flow_data = fetch_alpha_vantage_data("CASH_FLOW", ticker, api_key)

    income_reports = income_data.get(report_key, [])
    balance_sheet_reports = balance_sheet_data.get(report_key, [])
    cash_flow_reports = cash_flow_data.get(report_key, [])
    
    data_rows = []
    num_reports = min(len(income_reports), len(balance_sheet_reports), len(cash_flow_reports))
    
    if num_reports == 0:
        print(f"⚠️ Warning: No {period} data found for {ticker}.")
        return pd.DataFrame() 
        
    for i in range(num_reports):
        income_dict = income_reports[i]
        balance_sheet_dict = balance_sheet_reports[i]
        cash_flow_dict = cash_flow_reports[i]
        
        # --- Helper Values (for ratios) ---
        revenue = safe_convert_to_float(income_dict, "totalRevenue")
        net_income = safe_convert_to_float(income_dict, "netIncome")
        op_inc = safe_convert_to_float(income_dict, "operatingIncome")
        assets = safe_convert_to_float(balance_sheet_dict, "totalAssets")
        equity = safe_convert_to_float(balance_sheet_dict, "totalShareholderEquity")
        debt = safe_convert_to_float(balance_sheet_dict, "shortLongTermDebtTotal")
        curr_assets = safe_convert_to_float(balance_sheet_dict, "totalCurrentAssets")
        curr_liab = safe_convert_to_float(balance_sheet_dict, "totalCurrentLiabilities")
        cash = safe_convert_to_float(balance_sheet_dict, "cashAndCashEquivalentsAtCarryingValue")
        receivables = safe_convert_to_float(balance_sheet_dict, "currentNetReceivables")
        interest_exp = safe_convert_to_float(income_dict, "interestExpense") or 0
        cffo = safe_convert_to_float(cash_flow_dict, "operatingCashflow")
        capex = safe_convert_to_float(cash_flow_dict, "capitalExpenditures")

        row_data = {
            "Date": income_dict.get("fiscalDateEnding"),
            # --- Income Statement ---
            "Revenue": revenue,
            "COGS": safe_convert_to_float(income_dict, "costOfRevenue"),
            "Gross Margin": None, 
            "R&D": safe_convert_to_float(income_dict, "researchAndDevelopment"),
            "G&A": safe_convert_to_float(income_dict, "sellingGeneralAndAdministrative"),
            "OpEx": safe_convert_to_float(income_dict, "operatingExpenses"),
            "OpInc": op_inc,
            "Interest Expense": interest_exp,
            "Pretax Income": safe_convert_to_float(income_dict, "incomeBeforeTax"),
            "Taxes": safe_convert_to_float(income_dict, "incomeTaxExpense"),
            "Net Income": net_income,
            "EPS": safe_convert_to_float(income_dict, "reportedEPS"),
            "Shares": safe_convert_to_float(income_dict, "commonStockSharesOutstanding"),
            # --- Balance Sheet ---
            "Cash": cash,
            "AR": receivables,
            "PP&E": safe_convert_to_float(balance_sheet_dict, "propertyPlantEquipment"),
            "Goodwill": safe_convert_to_float(balance_sheet_dict, "goodwill"),
            "Total Current Assets": curr_assets,
            "Total Current Liabilities": curr_liab,
            "AP": safe_convert_to_float(balance_sheet_dict, "currentAccountsPayable"),
            "DR": safe_convert_to_float(balance_sheet_dict, "deferredRevenue"),
            "Debt": debt,
            "SE": equity,
            "Assets": assets,
            "L+SE": (safe_convert_to_float(balance_sheet_dict, "totalLiabilities") or 0) + (equity or 0),
            # --- Cash Flow ---
            "CFFO": cffo,
            "CapEx": capex,
            # --- TTM Placeholders (for quarterly) ---
            "TTM CFFO": None,
            "TTM Revenue": None,
            "TTM Net Income": None,
            # --- Calculated Ratios ---
            "Free Cash Flow": (cffo or 0) - (capex or 0),
            "Operating Margin": (op_inc / revenue) if op_inc and revenue else None,
            "Net Profit Margin": (net_income / revenue) if net_income and revenue else None,
            "ROE": (net_income / equity) if net_income and equity else None,
            "ROA": (net_income / assets) if net_income and assets else None,
            "Current Ratio": (curr_assets / curr_liab) if curr_assets and curr_liab else None,
            "Quick Ratio": ((cash or 0) + (receivables or 0)) / curr_liab if curr_liab else None,
            "Debt-to-Equity": (debt / equity) if debt and equity else None,
            "Interest Coverage": (op_inc / interest_exp) if op_inc and interest_exp > 0 else None,
        }

        if row_data["Revenue"] and row_data["COGS"]:
            row_data["Gross Margin"] = (row_data["Revenue"] - row_data["COGS"]) / row_data["Revenue"]

        data_rows.append(row_data)

    df = pd.DataFrame(data_rows)
    
    if df.empty:
        return df

    # --- Period-Specific Calculations (TTM, Growth) ---
    df = df.sort_values(by="Date", ascending=True).reset_index(drop=True)
    
    if period == 'quarterly':
        df['TTM CFFO'] = df['CFFO'].rolling(window=4, min_periods=4).sum()
        df['TTM Revenue'] = df['Revenue'].rolling(window=4, min_periods=4).sum()
        df['TTM Net Income'] = df['Net Income'].rolling(window=4, min_periods=4).sum()
        df['QoQ Revenue Growth'] = df['Revenue'].pct_change(periods=1)
        df['QoQ Net Income Growth'] = df['Net Income'].pct_change(periods=1)
        df['QoQ EPS Growth'] = df['EPS'].pct_change(periods=1)
        df = df.sort_values(by="Date", ascending=False).reset_index(drop=True)
    
    else: # Annual
        df['YoY Revenue Growth'] = df['Revenue'].pct_change(periods=1)
        df['YoY Net Income Growth'] = df['Net Income'].pct_change(periods=1)
        df['YoY EPS Growth'] = df['EPS'].pct_change(periods=1)
        df['YoY FCF Growth'] = df['Free Cash Flow'].pct_change(periods=1)
        
    df = df.set_index("Date").T

    if period == 'annual':
        df = df.sort_index(axis=1, ascending=True)

    # --- Formatting & Renaming ---
    ratio_rows = [
        "Gross Margin", "EPS", "Operating Margin", "Net Profit Margin", "ROE", "ROA",
        "Current Ratio", "Quick Ratio", "Debt-to-Equity", "Interest Coverage",
        "QoQ Revenue Growth", "QoQ Net Income Growth", "QoQ EPS Growth",
        "YoY Revenue Growth", "YoY Net Income Growth", "YoY EPS Growth", "YoY FCF Growth"
    ]
    metrics_to_convert = [idx for idx in df.index if idx not in ratio_rows]
    
    for metric in metrics_to_convert:
        try:
            df.loc[metric] = df.loc[metric].astype(float) / 1e9
        except Exception:
            pass

    rename_dict = {idx: f"{idx} (B$)" for idx in metrics_to_convert}
    df.rename(index=rename_dict, inplace=True)

    return df


def build_price_dataframe(ticker: str, api_key: str) -> pd.DataFrame:
    """
    Fetches daily adjusted stock prices.
    """
    print(f"Fetching stock price data for {ticker}...")
    json_data = fetch_alpha_vantage_data("TIME_SERIES_DAILY_ADJUSTED", ticker, api_key)
    
    price_data = json_data.get("Time Series (Daily)", {})
    if not price_data:
        print("⚠️ Warning: No price data found.")
        return pd.DataFrame()
        
    df = pd.DataFrame.from_dict(price_data, orient='index')
    
    df.rename(columns={
        "1. open": "Open", "2. high": "High", "3. low": "Low", 
        "4. close": "Close", "5. adjusted close": "Adj Close", 
        "6. volume": "Volume"
    }, inplace=True)
    
    df.index = pd.to_datetime(df.index)
    df.sort_index(ascending=True, inplace=True)
    
    for col in df.columns:
        df[col] = pd.to_numeric(df[col])
        
    return df