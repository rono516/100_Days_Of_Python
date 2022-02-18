import streamlit as st

st.write(""" # Stock Prediction App """)
st.title("  Streamlit")
st.header("Data Science App")
st.sidebar.header("Rono Collins \n Code Along With me")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import yfinance as fn

start = '2022-01-14'
end = '2022-01-14'


def get_ticker(name):
    company = fn.Ticker(name)
    return company


c1 = get_ticker("AAPL")
c2 = get_ticker("MSFT")
c3 = get_ticker("TSLA")

# fetching data for dataframe
apple = fn.download("AAPL", start, end)
microsoft = fn.download("MSFT", start, end)
tesla = fn.download("TSLA", start, end)

# fetching historical data by periods
data1 = c1.history(period="3mo")
data2 = c2.history(period="3mo")
data3 = c3.history(period="3mo")

# Mardkdown
st.write(""" ### Apple """)

# Detailed summary about Apple Company
st.write(c1.info['longBusinessSummary'])

# dataframe
st.write(apple)
# chart
st.line_chart(data1.values)

# Microsoft

# Mardkdown
st.write(""" ### Microsoft """)

# Detailed summary about Microsoft Company
st.write(c2.info['longBusinessSummary'])

# dataframe
st.write(microsoft)
# chart
st.line_chart(data2.values)

# Tesla

st.write(""" ### Tesla """)

# Detailed summary about Tesla Company
st.write(c3.info['longBusinessSummary'])

# dataframe
st.write(tesla)
# chart
st.line_chart(data3.values)
