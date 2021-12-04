# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 23:03:43 2021

@author: user
"""

import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def app():
    ########################################################
    # headers
    ########################################################
    
    # title
    st.title("Next WORD PREDICTION")
    
    # title
    st.sidebar.title("Result")
    
    # user inputs
    number = st.sidebar.slider("Select the number of words to predict :",1.0,10.0,5.0 )
    name = st.sidebar.text_input(label = "Enter the Word/letters")
    
    # submit
    if(st.sidebar.button("Submit")):
       
        # reset    
        st.button("Reset")
    
        
        
    
    
        
