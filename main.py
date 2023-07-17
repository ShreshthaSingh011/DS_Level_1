import streamlit as st
import yfinance as yf
import pandas as pd

st.write('''
        # Stock Price Application
        Shreshtha Singh''')

tickerSymbol = 'AAPL'
st.write('Company Code:', tickerSymbol)

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d',start='2010-5-31', end= '2020-5-31')
st.write('''
## Closing Price
''')
st.line_chart(tickerDf.Close)
st.write('''
## Volume Price
''')
st.line_chart(tickerDf.Volume)


