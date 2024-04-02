import streamlit as st
import utils.utils as ut
import utils.TextAnalyzer as te
import time

st.subheader('Analisi del testo')

json_config = ut.getJsonConfigFiles('dummy')
eng_list = ut.buildEngineList(json_config)

options = st.multiselect(
    'Seleziona il motore di analisi del testo',
    eng_list,
    [])

# st.write('Selezione:', options)

txt = st.text_area(
    "Testo da analizzare:",
    "Il Dr. Mario Rossi codice fiscale NRRRSS70E23H294A è invitato al convegno presso la MyCorp Inc. 00304260409 sulla attività recenti a Roma in via Salaria 100. Il suo indirizzo di posta elettronica è marco.rossi@libero.it ed ha il raffreddore ed anche l'influenza"
    )

# st.write(f'You wrote {len(txt)} characters.')

if st.button('Analizza'):
    st.write('Risultato:')
    response = te.TextAnalyzer(txt, json_config, options)
    # re ranking response ... and show
    # st.json(response)
    # te.DisplayResponse(response)
    # r_response = te.RerankResponse(response)

    for resp in response:
        st.json(response)
        st.text("Engine: " + resp["engine"] + " - description: " + resp["description"])
        st.dataframe(ut.json2DataFrame(resp["data"]))
    




# with st.spinner('Wait for it...'):
#     time.sleep(5)
# st.success('Done!')