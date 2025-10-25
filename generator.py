"""
generator.py

Main entry point for the Financial Data Exporter.

This script coordinates fetching data, building DataFrames, and exporting
to a formatted Excel file.

Usage:
    # 1. Set your API key as an environment variable:
    #    (PowerShell):  $env:ALPHA_VANTAGE_API_KEY="YOUR_KEY"
    #    (macOS/Linux): export ALPHA_VANTAGE_API_KEY="YOUR_KEY"
    #
    # 2. Run the script from your terminal:
    python generator.py YOUR_TICKER
"""

import argparse
import os
import sys

# Import our custom modules
from data_builder import fetch_summary_data, build_financials_dataframe, build_price_dataframe
from definitions import create_definitions_dataframe
from excel_exporter import export_to_excel

def main():
    """Main execution function to run the script."""
    
    # --- Setup CLI Argument Parser ---
    parser = argparse.ArgumentParser(description="Fetch financial data for a stock ticker.")
    parser.add_argument("ticker", type=str, help="The stock ticker symbol (e.g., AAPL)")
    parser.add_argument("-k", "--key", type=str, help="Your Alpha Vantage API key (optional, prefers env var)")
    args = parser.parse_args()
    
    ticker_symbol = args.ticker.strip().upper()
    
    # --- Get API Key ---
    api_key = args.key or os.environ.get('ALPHA_VANTAGE_API_KEY')
    if not api_key:
        print("❌ Error: API key not found.")
        print("Please pass the key with -k YOUR_KEY, or set the 'ALPHA_VANTAGE_API_KEY' environment variable.")
        sys.exit(1) # Exit with an error code

    print(f"📊 Fetching all financial data for {ticker_symbol}...")

    try:
        # --- 1. Fetch & Build Data ---
        # Note: API calls are implicitly made by the data_builder functions
        summary_df = fetch_summary_data(ticker_symbol, api_key)
        
        print("Fetching quarterly data...")
        quarterly_financials_df = build_financials_dataframe(ticker_symbol, api_key, 'quarterly')
        
        print("Fetching annual data...")
        annual_financials_df = build_financials_dataframe(ticker_symbol, api_key, 'annual')
        
        price_df = build_price_dataframe(ticker_symbol, api_key)
        
        definitions_df = create_definitions_dataframe()
        
        # --- 2. Export Data ---
        if not quarterly_financials_df.empty or not annual_financials_df.empty:
            export_to_excel(
                ticker_symbol, 
                summary_df, 
                quarterly_financials_df, 
                annual_financials_df, 
                price_df, 
                definitions_df
            )
        else:
            print(f"No financial statement data processed for {ticker_symbol}.")
            
    except Exception as error:
        print(f"❌ An error occurred: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()