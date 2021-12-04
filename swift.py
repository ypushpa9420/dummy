# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 00:43:41 2021

@author: Priya
"""
import streamlit as st
import pandas as pd
from multiapp import MultiApp
from apps import intro,result,plots

app = MultiApp()

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand"  target="_blank">SWIFTKEY PROJECT</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">INTRODUCTION<span class="sr-only">(current)</span></a>
      </li>
     <!-- <li class="nav-item">
        <a class="nav-link" href="/home.app" target="_blank">RESULT</a>
      </li>
 <li class="nav-item">
        <a class="nav-link" href="/data.app" target="_blank">PLOTS</a>
      </li>-->
       <li class="nav-item">
        <a class="nav-link" href="#" target="_blank">DOCUMENTATION</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)



st.title('**NEXT WORD / LETTER PREDICTOR**')


# Add all your application here
app.add_app("HOME", intro.app)
app.add_app("EDA and VDA", plots.app)
app.add_app("PREDICTION", result.app)
#app.add_app("PLOTS", plots.app)
#app.add_app("MODEL", model.app)
# The main app
app.run()




