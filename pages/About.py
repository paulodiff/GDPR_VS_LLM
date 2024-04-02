import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
     page_title='NER_APP',
     layout="wide",
     initial_sidebar_state="expanded",
)


st.header("About")

st.subheader("https://github.com/paulodiff/GDPR_VS_LLM/blob/main/README.md")


st.subheader("https://github.com/paulodiff/GDPR_VS_LLM/blob/main/README.md")


st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[TEXT2BOLD][:blue[LOC]] NoColor :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)


j = {
     "1":{
          "entity":"MISC",
          "score":"0.5",
          "index":1,
          "word":"awesome cool wonderful!",
          "start":0,
          "end":23
     },
     "2":{
     "entity":"PER",
     "score":"0.5",
     "index":2,
     "word":"Ernesto Rossi",
     "start":45,
     "end":58
     }
}

st.json(j)
