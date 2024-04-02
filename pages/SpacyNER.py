import spacy
import utils.utils as ut
from spacy.matcher import Matcher
from collections import Counter
from spacy import displacy
from random import choice

import streamlit as st

print("START SpacyNER:")


# nlp = spacy.load("it_core_news_sm")
nlp = spacy.load("it_core_news_lg")

# disabilita la pipe interna NER usa solo la ent
print("Spacy pipelines:", nlp.pipe_names)

# nlp.disable_pipes('ner')

# add entity_ruler pipe
config = {"overwrite_ents": True}
# ruler = nlp.add_pipe("entity_ruler", config=config)

my_list = [
'Il Dr. Mario Rossi codice fiscale NRRRSS70E23H294A è invitato al convegno presso la MyCorp Inc. 00304260409 sulla attività recenti a Roma in via Salaria 100. Il suo indirizzo di posta elettronica è marco.rossi@libero.it',
'Tanto va la gatta al lardo RGGRGR70A22J332W che ci lascia lo zampino a Salsomaggiore con il rafreddore',
'Buongiorno a tutti sono Luca Rossi cf: RGGRGR70A22J332W s:  AGGRGR70A11Y132M e  RGGRGR70A22J332W  di Napoli e vengo a proporre la mia partita iva 00304222409 e al mia email aaaa.rossi@gmail.com',
'Come tutti gli hanni Ernesto Rossi ha preso un lungo periodo di malattia a causa di un forte raffreddore, con l',
'awesome cool wonderful! Come tutti gli hanni Ernesto Rossi ha preso un lungo periodo di malattia a causa di un forte raffreddore',
'TEST MALATTIE: raffredore influuenza ottite'
]

for text in my_list:
  doc = nlp(text)

  print("Text:--------------------------------------------------------------------------------------")
  print(text)
  print("Ents:")
  # print(doc.ents)
  print([(ent.text, ent.label_, ent.start_char, ent.end_char) for ent in doc.ents])


  st.text(text)
  js = ut.spacyEnt2Json(text, doc.ents, "0.5")
  st.json(js)
  mk = ut.makeMarkdown(text,js,[])
  st.markdown(mk)






  #  for token in doc:
  #   print(token.text, token.pos_, token.dep_, token)
  # st.json(doc)
  # displacy.render(doc, style="ent", j, options=options)
  # print([(ent.text, ent.label_) for ent in doc.ents])upyter=True