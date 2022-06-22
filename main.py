import streamlit as st
from datetime import date

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go


START = 2015-1-1
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Paradox Stock App")

stocks = (PDX)

n_years = st.slider("Years of Prediction", 1 , 4)
period = n_years * 365