import yfinance as yf
import streamlit as st
import pandas as pd

st.write('''
# Simple Stoc Price App

Shown are the stock closing price and volume of Google!

''')
# Compañía de Minas Buenaventura S.A.A. (BVN)
# DEFINE THE TICKER SYMBOL
tickerSymbol = 'GOOG'
# GET DATA ON THIS TICKER
tickerData = yf.Ticker(tickerSymbol)
# GET THE HISTORICAL PRICES FOR THIS TICKER
tickerDF = tickerData.history(period='1d',start='2010-5-31',end='2023-7-1')
#OPEN HIGH  LOW CLOSE   VOLUME DIVIDENDS     STOCK SPLITS
st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)



