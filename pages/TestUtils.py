import utils.utils as ut
import streamlit as st
import json
import time

# print(ut.multiply(3, 4))

st.header('Test utils')
#st.text('Json test da Tranformer')


LMStudio = {
  "id": "chatcmpl-0chkynnkvhjrz35eq3oislf",
  "object": "chat.completion",
  "created": 1713269288,
  "model": "DeepMount00/Mistral-Ita-7b-GGUF/mistral_ita-7b-Q4_K_M.gguf",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": " Nome: Mario Rossi\nCognome: Rossi\nQualifica professionale: Dr. (Dottore)\nNome completo per codice fiscale: Mario Rossi\nCodice fiscale: NRRRSS70E23H294A\nEvento: Convegno\nOrganizzazione: MyCorp Inc.\nCodice identificativo MyCorpo: 00304260409\nLuogo: Roma, in via Salaria 100\nInformazioni di salute: ha il raffreddore e l'influenza\nIndirizzo email: marco.rossi@libero.it"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 159,
    "completion_tokens": 158,
    "total_tokens": 317
  }
}

LM1 = {
 'id': 'chatcmpl-bfe6218f24o498ayj8mcpm', 
 'object': 'chat.completion', 
 'created': 1713282053, 
 'model': 'DeepMount00/Mistral-Ita-7b-GGUF/mistral_ita-7b-Q4_K_M.gguf', 
 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': " Nome: Mario Rossi\nCognome: Rossi\nQualifica professionale: Dr. (Dottoре)\nNascita: Assente dallo scenario fornito, ma il cognome suggerisce un'origine italiana\nSesso: Non indicato\nData di nascita: Assente\nIndirizzo: Assente\nProvincia/Regione: Assente\nStato/Nazione: Assente\nCittà: Roma\nStrada/Via: Via Salaria 100\nOrganizzazione o Instituzione associata (sito del convegno): MyCorp Inc.\nCodice fiscale: NRRRSS70E23H294A\nCodice fiscale significa: In contesto italiano e europeo, il codice fiscale è un identificatore di tassazione utilizzato per individuare l'entità tributaria.\nEmail: marco.rossi@libero.it\nStato di salute: Raffreddore e influenza (malattie virali)"}, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 246, 'completion_tokens': 245, 'total_tokens': 491}}


#st.text('formatLMStudioResponse')
out = ut.formatLMStudioResponse(LM1)

st.write(out)






resp = {
  "engine": "LMStudio",
  "description": "LMStudio - Mistral-7B-Instruct-v0.1-GGUF",
  "data": [
    {
      "description": "Nome",
      "value": "Mario Rossi"
    },
    {
      "description": "Cognome",
      "value": "Rossi"
    },
    {
      "description": "Professione",
      "value": "Dr."
    },
    {
      "description": "Attività medica o professionale",
      "value": "Non specificato nel testo"
    },
    {
      "description": "Codice fiscale",
      "value": "NRRRSS70E23H294A"
    },
    {
      "description": "Evento",
      "value": "Convegno"
    },
    {
      "description": "Organizzazione",
      "value": "MyCorp Inc."
    },
    {
      "description": "Numero identificativo dell'organizzazione",
      "value": "00304260409"
    },
    {
      "description": "Luogo dell'evento",
      "value": "Roma, via Salaria 100"
    },
    {
      "description": "Indirizzo di posta elettronica",
      "value": "marco.rossi@libero.it"
    },
    {
      "description": "Malattie personali temporanee",
      "value": "Raffreddore e influenza"
    },
    {
      "description": "Informazioni aggiuntive",
      "value": "Nessuna altra informazione personale rilevabile nel testo fornito."
    }
  ]
}



# st.json(resp)
# st.dataframe(ut.json2DataFrameHF(resp["data"]), use_container_width=True)


spacy = {
  "engine": "spacy",
  "description": "Spacy_List",
  "data": {
    "1": {
      "entity": "NOMI",
      "score": 1,
      "index": 1,
      "word": "Mario",
      "start": 7,
      "end": 12
    },
    "2": {
      "entity": "COGNOMI",
      "score": 1,
      "index": 2,
      "word": "Rossi",
      "start": 13,
      "end": 18
    },
    "3": {
      "entity": "LOCALITA",
      "score": 1,
      "index": 3,
      "word": "Roma",
      "start": 133,
      "end": 137
    },
    "4": {
      "entity": "MALATTIE",
      "score": 1,
      "index": 4,
      "word": "raffreddore",
      "start": 229,
      "end": 240
    }
  }
}

st.json(spacy)

j_s = ut.jsonSpacy(spacy["data"])

st.json(j_s)
st.dataframe(j_s, use_container_width=True)





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
 

# st.json(jHF)

# st.text('Json patch al campo score')

# jPatched = ut.jsonPatchScoreField(jHF["data"])

# print(jPatched)
# st.json(jPatched)

# st.text('Json a identificativo int to string...')

# jPHF = ut.jsonPatchHF(json.loads(jPatched))
# print(jPHF)
# st.json(jPHF)


# st.text('DATA_FRAME')
# st.dataframe(ut.json2DataFrame(j),use_container_width=True)
# st.text('DATA_FRAME_HF')
# st.dataframe(ut.json2DataFrameHF(j2["data"]),use_container_width=True)

# st.json(ut.jsonPatchHF(j2["data"]))

# st.write('Path json from Huggingface')


