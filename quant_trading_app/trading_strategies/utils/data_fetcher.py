import pandas as pd
import yfinance as yf

def fetch_yfinance_data(ticker, start_date, end_date):
    """
    Fetches historical stock data from Yahoo Finance.
    """
    return yf.download(ticker, start=start_date, end=end_date)
