import requests
import streamlit as st

URL = "http://localhost:1234/v1/chat/completions"


txt = st.text_area(
    "Testo da analizzare:",
    "Il Dr. Mario Rossi codice fiscale NRRRSS70E23H294A è invitato al convegno presso la MyCorp Inc. 00304260409 sulla attività recenti a Roma in via Salaria 100. Il suo indirizzo di posta elettronica è marco.rossi@libero.it ed ha il raffreddore ed anche l'influenza"
    )

prompt = "Elenca i dati personali della seguente frase:" + txt


PARAMS = { 
    "model": "TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
    "messages": [ 
      { "role": "system", "content": "Always answer in rhymes." },
      { "role": "user", "content": "Introduce yourself." }
    ], 
    "temperature": 0.7, 
    "max_tokens": -1,
    "stream": True
}

st.write(PARAMS)

if st.button('Analizza'):
    
    print(txt)
    prompt = "Elenca i dati personali della seguente frase:" + txt
    print(prompt)
    DATA = { 
        "model": "DeepMount00/Mistral-Ita-7b-GGUF",
        "prompt" : prompt,
        "messages": [
            { "role": "system", "content": "Rispondi sempre correttamente." },
            { "role": "user", "content": prompt }
        ],
        "temperature": 0.7, 
        "max_tokens": -1,
        "stream": False
    }
    st.write(DATA)
    
    with st.spinner('Wait for it...'):
        r = requests.post(url=URL, json=DATA)

    data = r.json()
    st.write(data)
    print(data)


#[2024-04-16 09:53:07.134] [INFO] [LM STUDIO SERVER] ->	GET  http://localhost:1234/v1/models
#[2024-04-16 09:53:07.135] [INFO] [LM STUDIO SERVER] ->	POST http://localhost:1234/v1/chat/completions
#[2024-04-16 09:53:07.135] [INFO] [LM STUDIO SERVER] ->	POST http://localhost:1234/v1/completions
#[2024-04-16 09:53:07.136] [INFO] [LM STUDIO SERVER] ->	POST http://localhost:1234/v1/embeddings     <------------ NEW!
#[2024-04-16 09:53:07.136] [INFO] [LM STUDIO SERVER] Model loaded: TheBloke/Mistral-7B-Instruct-v0.1-GGUF/mistral-7b-instruct-v0.1.Q2_K.gguf

#prompt = f
#Context information is below.
#---------------------
#{retrieved_chunk}
#---------------------
#Given the context information and not prior knowledge, answer the query.
#Query: {question}
#Answer:

