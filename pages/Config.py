import streamlit as st
import os
import subprocess
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import utils.utils as ut

st.set_page_config(
     page_title='NER_APP',
     layout="wide",
     initial_sidebar_state="expanded",
)


st.header("Config")

st.text("Pagina di configurazione")


st.subheader("Liste")


st.subheader("Espressioni regolari")


st.subheader("Modelli")


st.text("Huggingface - Spacy - LLM (Mistral) ecc.")

# output = os.system("spacy info")

# st.text(output)


st.subheader("Loading ... info ... wait!")

# output = subprocess.check_output("spacy info")

# str_out = output.decode("utf-8")

st.subheader("Spacy1")
# st.code(str_out)


st.subheader("Huggingface")

jj = ut.getJsonConfigFiles('dummy')

st.json(jj)

st.text(ut.buildEngineList(jj))


