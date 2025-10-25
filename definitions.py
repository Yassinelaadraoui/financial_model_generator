"""
definitions.py

Contains the definitions for all financial metrics.
"""

import pandas as pd

def create_definitions_dataframe() -> pd.DataFrame:
    """Creates a DataFrame containing definitions for key financial metrics."""
    definitions_map = {
        # --- Base Metrics ---
        "Revenue": "Total sales before any costs are deducted.",
        "COGS": "Cost of goods sold – direct costs of producing goods/services.",
        "Gross Margin": "Profit after COGS, as a percentage of revenue.",
        "R&D": "Research & Development expenses.",
        "G&A": "General & Administrative overhead costs.",
        "OpEx": "Operating expenses (R&D + G&A).",
        "OpInc": "Operating income (Gross profit – OpEx).",
        "Net Income": "Final profit after taxes.",
        "EPS": "Earnings per share (Net Income / Shares).",
        "Shares": "Weighted average shares outstanding.",
        "Cash": "Cash and equivalents.",
        "AR": "Accounts receivable – customer balances.",
        "PP&E": "Property, Plant & Equipment.",
        "Goodwill": "Premium paid on acquisitions.",
        "AP": "Accounts Payable.",
        "DR": "Deferred Revenue.",
        "Debt": "Short + Long-term debt.",
        "SE": "Shareholders’ Equity.",
        "Assets": "Total company assets.",
        "CFFO": "Cash Flow From Operations.",
        "CapEx": "Capital Expenditures (investments in assets like PP&E).",
        # --- Calculated Ratios & Metrics ---
        "Free Cash Flow": "CFFO - CapEx. Cash available after funding operations and capital projects.",
        "Operating Margin": "Operating Income / Revenue. Core business profitability.",
        "Net Profit Margin": "Net Income / Revenue. Overall profitability after all expenses.",
        "ROE": "Return on Equity (Net Income / Shareholders' Equity). Profit generated with shareholder money.",
        "ROA": "Return on Assets (Net Income / Total Assets). Profit generated from all assets.",
        "Current Ratio": "Total Current Assets / Total Current Liabilities. Short-term liquidity.",
        "Quick Ratio": "(Cash + Accts. Receivable) / Total Current Liabilities. Stricter liquidity test.",
        "Debt-to-Equity": "Total Debt / Shareholders' Equity. Financial leverage/risk.",
        "Interest Coverage": "Operating Income / Interest Expense. Ability to pay interest on debt.",
        # --- Growth Rates ---
        "YoY Growth": "Year-over-Year growth percentage.",
        "QoQ Growth": "Quarter-over-Quarter growth percentage.",
        # --- Summary Page Metrics ---
        "MarketCapitalization": "Total market value of the company's outstanding shares.",
        "EBITDA": "Earnings Before Interest, Taxes, Depreciation, and Amortization.",
        "PERatio": "Price-to-Earnings Ratio. Market price per share / EPS.",
        "PEGRatio": "P/E Ratio / EPS Growth Rate. Valuation adjusted for growth.",
        "PriceToBookRatio": "Market Cap / Book Value (Shareholders' Equity).",
        "DividendYield": "Annual dividend per share / Price per share.",
        "PayoutRatio": "Percentage of earnings paid out as dividends.",
        "EVToEBITDA": "Enterprise Value / EBITDA. A common valuation metric.",
    }
    return pd.DataFrame(definitions_map.items(), columns=["Metric", "Definition"])