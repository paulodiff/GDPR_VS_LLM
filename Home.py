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

st.subheader("NER Named Entity Recognition text analyzer")


st.text("https://github.com/paulodiff/GDPR_VS_LLM/blob/main/README.md")



st.subheader("Analisi del testo per riconoscere e sottolineare entità da oscurare per essere sottoposte ad un LLM")

