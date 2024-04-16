# NER_APP
# APP per la gestione dei dati personali
# https://github.com/paulodiff/GDPR_VS_LLM/blob/main/README.md

# Esegue con:  streamlit run home.py


import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
     page_title='NER_APP',
     layout="wide",
     initial_sidebar_state="expanded",
)


st.header("Home")

st.image('logo.png', caption='LOGO')

# open and display README.md
with open('README.md') as f: s = f.read()
st.markdown(s)



     

st.subheader("GDPR text analyze")

st.text("Github: https://github.com/paulodiff/GDPR_VS_LLM/blob/main/README.md")

st.text("Analisi del testo per riconoscere e sottolineare dati personali prima di inviarli ad un LLM")

