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

[data-testid="stToolbar"] {{
right: 2rem;
}}

</style>

"""


st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("OUR VENTURE")
st.write("We are here to completly change the trading game here.we are going to help you with saving your expensive time by aotomating the old school way of trading by automating the trendline. and it is gonna save you days and days of work gonna make those trend lines and with the help of rsi(relative index indicator).it is gonna help you make that descision wheter you are gonna take that trade or not.it is absolutely beginner friendly too")



def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_hello = load_lottieurl(
    "https://assets5.lottiefiles.com/packages/lf20_Vs1dk5.json")

st_lottie(lottie_hello,
        #   height="10rem",
        #   width="10rem",

          key="hello")