# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:57:46 2018

@author: Administrator
"""

import numpy as np
import pandas as pd
from ..utils.data_fetcher import fetch_yfinance_data
from ..utils.plotting import plot_backtest

def macd(signals, ma1, ma2):
    signals['ma1'] = signals['Close'].rolling(window=ma1, min_periods=1, center=False).mean()
    signals['ma2'] = signals['Close'].rolling(window=ma2, min_periods=1, center=False).mean()
    return signals

def signal_generation(df, method, ma1, ma2):
    signals = method(df, ma1, ma2)
    signals['positions'] = 0
    signals['positions'][ma1:] = np.where(signals['ma1'][ma1:] >= signals['ma2'][ma1:], 1, 0)
    signals['signals'] = signals['positions'].diff()
    signals['oscillator'] = signals['ma1'] - signals['ma2']
    return signals

def run_macd_backtest(ticker, start_date, end_date, ma1, ma2, slicer=0):
    """
    Runs the MACD backtest.
    """
    df = fetch_yfinance_data(ticker, start_date, end_date)
    new = signal_generation(df, macd, ma1, ma2)
    new = new[slicer:]
    return plot_backtest(new, ticker)

if __name__ == '__main__':
    # Example usage:
    run_macd_backtest('AAPL', '2020-01-01', '2021-01-01', 10, 21)
