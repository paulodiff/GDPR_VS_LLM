from transformers import AutoModelForTokenClassification, AutoTokenizer
from transformers import pipeline
import streamlit as st
import os
import subprocess
import pandas as pd
import numpy as np
import json
import re
import string
from spacy import displacy


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):

        if isinstance(obj, np.floating):
          return str(obj)

        if isinstance(obj, str):
            return obj

        return json.JSONEncoder.default(self, obj)


"""
tokenizer = AutoTokenizer.from_pretrained("osiria/deberta-base-italian-uncased-ner")
model = AutoModelForTokenClassification.from_pretrained("osiria/deberta-base-italian-uncased-ner", num_labels = 5)
"""
from transformers import AutoModel, AutoTokenizer

model_name = "DeepMount00/Italian_NER_XXL"

# Load model directly
from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("DeepMount00/Italian_NER_XXL")
model = AutoModelForTokenClassification.from_pretrained("DeepMount00/Italian_NER_XXL")

text = 'Il Dr. Mario Rossi codice fiscale NRRRSS70E23H294A è invitato al convegno presso la MyCorp Inc. 00304260409 sulla attività recenti a Roma in via Salaria 100. Il suo indirizzo di posta elettronica è marco.rossi@libero.it',


# my_list = [
# 'Il Dr. Mario Rossi codice fiscale NRRRSS70E23H294A è invitato al convegno presso la MyCorp Inc. 00304260409 sulla attività recenti a Roma in via Salaria 100. Il suo indirizzo di posta elettronica è marco.rossi@libero.it',
# 'Tanto va la gatta al lardo RGGRGR70A22J332W che ci lascia lo zampino a Salsomaggiore',
# 'Buongiorno a tutti sono Luca Rossi cf: RGGRGR70A22J332W s:  AGGRGR70A11Y132M e  RGGRGR70A22J332W  di Napoli e vengo a proporre la mia partita iva 00304222409 e al mia email aaaa.rossi@gmail.com'
# ]

ner = pipeline("ner", model=model, tokenizer=tokenizer)
ner_results = ner(text)

st.text(text)
st.json(ner_results)

ner_results_encoded = json.dumps(ner_results , cls=CustomEncoder)
data = json.loads(ner_results_encoded)
df = pd.json_normalize(data)

st.dataframe(df)

# for text in my_list:
#   print(text)
#  ner(text, aggregation_strategy="simple")

