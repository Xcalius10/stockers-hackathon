import json
import numpy as np
import pandas as pd
import yfinance
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
from PIL import Image
from datetime import datetime
import requests  # pip install requests
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import base64
st.set_option('deprecation.showPyplotGlobalUse', False)

@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("image1.jpg")

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
 background-color: red;
 opacity:0.8;
 background-image: url("https://images.pexels.com/photos/90764/man-studio-portrait-light-90764.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
 background-size: cover
 

}

[data-testid="stHeader"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-color: rgba(0,0,0,0);
background-repeat: no-repeat;
background-attachment: fixed;
}}

 [data-testid="stSidebarNav"] {
                    background-image: url("data:image/png;base64,{}");
                    background-repeat: no-repeat;
                    background-position: center;
                    margin-top: 10px;
                    background-size: %s %s;
                }

</style>

"""


st.markdown(page_bg_img, unsafe_allow_html=True)


st.sidebar.success("Direct to desired route")

PAGE_DICT = {
    "Home": "home",
    "About": "about"
}


def home():
    st.write("This is the home page.")


def about():
    st.write("This is the about page.")


# def docs():
#     st.write("This is the docs page.")


def main():
    st.title("Streamlit Navigation Bar Example")

    page = st.sidebar.selectbox("Select a page", list(PAGE_DICT.keys()))

    if page == "Home":
        home()
    elif page == "About":
        about()
    elif page == "Docs":
        docs()


if __name__ == "_main_":
    main()


st.title("Stockers")
user_input = st.text_input("Enter stock symbol", "VEDL.NS")
symb = yfinance.Ticker(user_input)

# ticker_name = yfinance.Ticker(user_input)

period_option = st.selectbox(
    'Period', {'1y', '1d', '1wk', '1mo', '3mo', '6mo', '2y', '5y'})
st.write('You selected:', period_option)

hist = symb.history(period=period_option)

pl1 = list(hist['High'])
res1 = max(pl1) - min(pl1)
#print(res1)

reg2p = np.round_(res1 * 2)/100
reg3p = np.round_(res1 * 3)/100
reg5p = np.round_(res1 * 5)/100
#print(reg2p, reg3p, reg5p)

num1 = 0
def regre2(num1):
    num2 = num1 + ((num1 * 2)/100)
    print(num2)

def regre3(num1):
    num2 = num1 + ((num1 * 3.5)/100)
    print(num2)

def regre5(num1):
    num2 = num1 + ((num1 * 5)/100)
    print(num2)
    
#print(regre2(min(pl1)), regre3(min(pl1)), regre5(min(pl1)))
l1 = np.round_(pl1)
l2 = sorted(l1)


from collections import Counter
data = Counter(l2)
a = data.most_common(10)
for (price, freq) in a:
    a0 = a[0][0]
    a1 = a[1][0]
    a2 = a[2][0]
    a3 = a[3][0]
    a4 = a[4][0]
    a5 = a[5][0]
    a6 = a[6][0]
    a7 = a[7][0]
    a8 = a[8][0]
    a9 = a[9][0]
print(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9)
symbol = symb

change = hist["High"].diff()
change.dropna(inplace=True)


# Create two copies of the Closing price Series
change_up = change.copy()
change_down = change.copy()

change_up[change_up<0] = 0
change_down[change_down>0] = 0

# Verify that we did not make any mistakes
change.equals(change_up+change_down)

# Calculate the rolling average of average up and average down
avg_up = change_up.rolling(14).mean()
avg_down = change_down.rolling(14).mean().abs()


rsi = 100 * avg_up / (avg_up + avg_down)

# Take a look at the 20 oldest datapoints
#rsi.head(20)

plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (20, 15)

ax1 = plt.subplot2grid((10,1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((10,1), (6,0), rowspan = 2, colspan = 1)

# First chart:
# Plot the closing price on the first chart
ax1.plot(hist['Close'], linewidth=2)
ax1.set_title('Close Price')

# Second chart
# Plot the RSI
ax2.set_title('Relative Strength Index')
ax2.plot(rsi, color='purple', linewidth=1)
# Add two horizontal lines, signalling the buy and sell ranges.
# Oversold
ax2.axhline(30, linestyle='--', linewidth=1.5, color='green')
# Overbought
ax2.axhline(70, linestyle='--', linewidth=1.5, color='red')
ax1.axhline(y = a0, color = 'b', linewidth=15, linestyle = '-', alpha = 0.3)
ax1.axhline(y = a1, color = 'b', linewidth=15, linestyle = '-', alpha = 0.3)
ax1.axhline(y = a2, color = 'b', linewidth=15, linestyle = '-', alpha = 0.3)
ax1.axhline(y = a3, color = 'b', linewidth=15, linestyle = '-', alpha = 0.3)
ax1.axhline(y = a4, color = 'b', linewidth=15, linestyle = '-', alpha = 0.3)
ax1.axhline(y = a5, color = 'b', linewidth=15, linestyle = '-', alpha = 0.3)
ax1.axhline(y = a6, color = 'b', linewidth=15, linestyle = '-', alpha = 0.3)
ax1.axhline(y = a7, color = 'b', linewidth=15, linestyle = '-', alpha = 0.3)
ax1.axhline(y = a8, color = 'b', linewidth=15, linestyle = '-', alpha = 0.3)
ax1.axhline(y = a9, color = 'b', linewidth=15, linestyle = '-', alpha = 0.3)







# rsi = 100 * avg_up / (avg_up + avg_down)

# # Take a look at the 20 oldest datapoints
# # rsi.head(20)
# # Set the theme of our chart
# plt.style.use('fivethirtyeight')

# # Make our resulting figure much bigger
# plt.rcParams['figure.figsize'] = (20, 15)

# # Create two charts on the same figure.
# ax1 = plt.subplot2grid((10, 1), (0, 0), rowspan=5, colspan=1)
# ax2 = plt.subplot2grid((10, 1), (6, 0), rowspan=2, colspan=1)

# # First chart:
# # Plot the closing price on the first chart
# ax1.plot(df_btc['Close'], linewidth=2)
# ax1.set_title('Close Price')

# # Second chart
# # Plot the RSI
# ax2.set_title('Relative Strength Index')
# ax2.plot(rsi, color='orange', linewidth=1)
# # Add two horizontal lines, signalling the buy and sell ranges.
# # Oversold
# ax2.axhline(30, linestyle='--', linewidth=1.5, color='green')
# # Overbought
# ax2.axhline(70, linestyle='--', linewidth=1.5, color='red')
# # plt.plot(df_btc,color=col)
# # plt.style.use("dark_background")
# # plt.plot(fig2)

# # st.pyplot()
# ax1.axhline(y=1610, color='b', linewidth=15, linestyle='-', alpha=0.3)
# #ax1.axhline(y = 1528, color = 'b', linewidth=15, linestyle = '-', alpha = 0.3)
# ax1.axhline(y=1489, color='b', linewidth=15, linestyle='-', alpha=0.3)
# ax1.axhline(y=1341, color='b', linewidth=15, linestyle='-', alpha=0.3)
# ax1.axhline(y=1293, color='b', linewidth=15, linestyle='-', alpha=0.3)
# plt.style.use("dark_background")




st.pyplot()



st.set_option('deprecation.showPyplotGlobalUse', False)

# st.button(label="return",on_click="")


# page_bg_img=""""""
