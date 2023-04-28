#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:29:37 2023

@author: gleveque
"""

# https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader
# https://docs.streamlit.io/library/api-reference/widgets

# TO DO:
    # Regarder pour mettre des photos cote à cote 

import streamlit as st
import pandas as pd
import pygwalker as pyg

st.set_page_config(layout="wide")
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

process_start = 0

count=1
uploaded_file = st.file_uploader("Choose a excel", key=count)
count+=1
if uploaded_file is not None:
    dataframe = pd.read_excel(uploaded_file)
    st.write(dataframe.head())
    
    process_start = 1
    

gwalker = pyg.walk(dataframe, env='Streamlit')
