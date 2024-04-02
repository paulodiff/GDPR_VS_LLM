import spacy
from spacy.matcher import Matcher
from collections import Counter
from spacy import displacy
from random import choice

import streamlit as st

# nlp = spacy.load("it_core_news_sm")
nlp = spacy.load("it_core_news_lg")

# disabilita la pipe interna NER usa solo la ent
print("Spacy pipelines:", nlp.pipe_names)

nlp.disable_pipes('ner')

# add entity_ruler pipe
config = {"overwrite_ents": True}
ruler = nlp.add_pipe("entity_ruler", config=config)

# sample data list
cognomi = ["Rossi", "Bianchi", "Verdi"]
nomi = ["Mario", "Luca", "Giovanni"]
localita = ["Milano", "Roma", "Salsomaggiore"]
malattie = ["raffreddore", "influenza", "otite"]


patterns = [
    {"label": "EML", "pattern": [{'LIKE_EMAIL': True}] },
    {"label": "CF_", "pattern": [{"TEXT" : {"REGEX": "^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$"}}]},
    {"label": "TARGA_AUTO", "pattern": [{"TEXT" : {"REGEX": "^[A-Z]{2}[0-9]{3}[A-Z]{2}$"}}]},
    {"label": "PI_", "pattern": [{"TEXT" : {"REGEX": "^[0-9]{11}$"}}]},
    {"label": "NNN", "pattern": [{"LEMMA": {"IN": nomi}}]},
    {"label": "CCC", "pattern": [{"LEMMA": {"IN": cognomi}}]},
    {"label": "LOC_1", "pattern": [{"LEMMA": {"IN": localita}}]},
    {"label": "DIS2_FZ", "pattern": [{"LEMMA": {"FUZZY": {"IN": malattie}}}] },
]


ruler.add_patterns(patterns)

my_list = [
'Il Dr. Mario Rossi codice fiscale NRRRSS70E23H294A è invitato al convegno presso la MyCorp Inc. 00304260409 sulla attività recenti a Roma in via Salaria 100. Il suo indirizzo di posta elettronica è marco.rossi@libero.it',
'Tanto va la gatta al lardo RGGRGR70A22J332W che ci lascia lo zampino a Salsomaggiore con il rafreddore',
'Buongiorno a tutti sono Luca Rossi cf: RGGRGR70A22J332W s:  AGGRGR70A11Y132M e  RGGRGR70A22J332W  di Napoli e vengo a proporre la mia partita iva 00304222409 e al mia email aaaa.rossi@gmail.com',
'Come tutti gli hanni Ernesto Rossi ha preso un lungo periodo di malattia a causa di un forte raffreddore, con l',
'awesome cool wonderful! Come tutti gli hanni Ernesto Rossi ha preso un lungo periodo di malattia a causa di un forte raffreddore',
'TEST MALATTIA: raffredore influuenza ottite'
]

for text in my_list:
  doc = nlp(text)
  print("Text:")
  print(text)
  print("Ents:")
  print(doc.ents)
  print([(ent.text, ent.label_, ent) for ent in doc.ents])
  # st.json(doc)
  # displacy.render(doc, style="ent", j, options=options)
  # print([(ent.text, ent.label_) for ent in doc.ents])upyter=True