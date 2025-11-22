
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import yfinance as yf


st.title("Market Analysis 🚀")
symbol_options = ['AAPL', 'BOC', 'SHEL', 'UNH' ]
global_symbol_options = ['^N225','^GDAXI', '^HSI']

def welcome_page():
  st.header("Welcome to my first app in Data Engineering")

def price_page():
# Create ticker object
  selected_ticker = st.selectbox('Select Stock Symbol', symbol_options)
  start_date_value = st.date_input("Select starting date", value=datetime(2015, 7, 1))
  end_date_value = st.date_input("Select end date", value=datetime(2019, 7, 31))

  if st.button("Show"):
    symbol_data = yf.Ticker(selected_ticker)
    hist = symbol_data.history(start=str(start_date_value), end=str(end_date_value))
    st.area_chart(hist['Close'])

def news_page():
# Create ticker object

  selected_ticker = st.selectbox('Select Stock Symbol', symbol_options)

  if st.button("Show"):
    # symbol_ticker = yf.Ticker(selected_ticker)
    ticker = yf.Ticker(selected_ticker)
    news = ticker.get_news()
    news_df = pd.json_normalize(news)
    news_df.head()

    for i in range(len(news_df)):
      st.subheader(news_df['content.title'][i])
      st.write(news_df['content.summary'][i])
      st.write(news_df['content.clickThroughUrl.url'][i])
      try:
        st.image(news_df['content.thumbnail.originalUrl'][i], width=200)
      except:
        pass
      st.divider()


def index_page():
    selected_global_ticker = st.selectbox('Select Index Symbol', global_symbol_options)

    if st.button("Show Index Info"):
        index_ticker = yf.Ticker(selected_global_ticker)
        index_hist = index_ticker.history(period="2d")

        if len(index_hist) >= 2:
            prev_close = index_hist["Close"].iloc[-2]
            last_close = index_hist["Close"].iloc[-1]
            change = last_close - prev_close
            change_pct = (change / prev_close) * 100

            st.write(f"{selected_global_ticker} Index Information")
            st.write(f"Previous close: {prev_close:.2f}")
            st.write(f"Last close:     {last_close:.2f}")
            st.write(f"Change:         {change:+.2f} ({change_pct:+.2f}%)")
        else:
            st.write("Not enough data returned for the selected index.")


pages= {}
pages["welcome_page"] = "Welcome"
pages["price_page"] = "Historical Prices"
pages["news_page"] = "News "
pages["index_page"] = "Global Indices"

if "current_page" not in st.session_state:
    st.session_state["current_page"] = "welcome_page"
    welcome_page()

elif st.session_state.current_page == "welcome_page":
    welcome_page()

elif st.session_state.current_page == "price_page":
    price_page()

elif st.session_state.current_page == "news_page":
    news_page()     

elif st.session_state.current_page == "index_page":
    index_page()


def sidebar_navigation():
    with st.sidebar:
        st.markdown("### Menu")
        if st.button(pages["welcome_page"]):
            st.session_state.current_page = "welcome_page";
            st.rerun()

        if st.button(pages["news_page"]):
            st.session_state.current_page = "news_page";
            st.rerun()

        if st.button(pages["price_page"]):
            st.session_state.current_page = "price_page";
            st.rerun()

        if st.button(pages["index_page"]):
            st.session_state.current_page = "index_page";
            st.rerun()


sidebar_navigation();


