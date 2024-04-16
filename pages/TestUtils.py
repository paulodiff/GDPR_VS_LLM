import utils.utils as ut
import streamlit as st
import json

# print(ut.multiply(3, 4))

st.header('Test utils')

st.text('Json test da Tranformer')

jHF = {
    "data" : 
    [
     {
     "entity":"MISC2",
     "score":0.111,
     "index":1,
     "word":"awesome cool wonderful!",
     "start":0,
     "end":23
     },
     {
     "entity":"PER2",
     "score":0.1225,
     "index":2,
     "word":"Ernesto Rossi",
     "start":45,
     "end":58
     }
    ]
}
 

st.json(jHF)

st.text('Json patch al campo score')

jPatched = ut.jsonPatchScoreField(jHF["data"])

print(jPatched)
st.json(jPatched)

st.text('Json a identificativo int to string...')


jPHF = ut.jsonPatchHF(json.loads(jPatched))
print(jPHF)
st.json(jPHF)


# st.text('DATA_FRAME')
# st.dataframe(ut.json2DataFrame(j),use_container_width=True)
# st.text('DATA_FRAME_HF')
# st.dataframe(ut.json2DataFrameHF(j2["data"]),use_container_width=True)

# st.json(ut.jsonPatchHF(j2["data"]))

# st.write('Path json from Huggingface')
