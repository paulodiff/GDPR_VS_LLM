import utils.utils as ut
import streamlit as st

# print(ut.multiply(3, 4))

st.header('Test utils')

text = 'awesome cool wonderful! Come tutti gli Hanni Ernesto Rossi ha preso un lungo periodo di malattia a causa di un forte raffreddore'
ents = [('awesome cool wonderful!', 'MISC', 0), ('Ernesto Rossi', 'PER', 45)]
score = "0.5"


# print(ut.spacyEnt2Json(text,ents,score))
# 
# st.text(t)
# st.json(e)

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

st.text(text)
mk = ut.makeMarkdown(text,j,[])

print(mk)

st.markdown(mk)

st.json(j)

