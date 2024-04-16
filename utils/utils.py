import streamlit as st
import json
import os
import pandas as pd
import numpy as np
import json

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):

        if isinstance(obj, np.floating):
          return str(obj)

        if isinstance(obj, str):
            return obj

        return json.JSONEncoder.default(self, obj)



def getAppConfig(configPath):
    # D:\NLP_AI_NER\NER_APP\config\app_config\*.json
    # json_folder_path = os.path.join("D:\\", "NLP_AI_NER", "NER_APP", "config", "app_config")
    # json_file_path = os.path.join(json_folder_path, "app.json") 

    json_file_path = st.secrets.app.appConfigFile


    # print('getAppConfig read:' + json_file_path)
    with open(json_file_path) as file:
      data = json.load(file)
      return data

def saveAppConfig(data):
    print('>>>saveAppConfig')
    print(data)
    # json_folder_path = os.path.join("D:\\", "NLP_AI_NER", "NER_APP", "config", "app_config")
    # json_file_path = os.path.join(json_folder_path, "app.json") 

    json_file_path = st.secrets.app.appConfigFile

    with open(json_file_path, 'w') as f:
      json.dump(data, f)
   
def updateAppConfigAddEngine(engineId):
    print('>>>updateAppConfigAddEngine')
    print(engineId)
    # reload ...
    jc = getAppConfig('')
    jc["engine_config"].append({
       "engine_id": engineId, 
       "enable": False
    })
    saveAppConfig(jc)   

def updateAppConfig(data):
    # D:\NLP_AI_NER\NER_APP\config\app_config\*.json
    print('>>>updateAppConfig')
    print(data)
    print('>>>updateAppConfig remove item?')


    # reload ...
    jc = getAppConfig('')
    jc["engine_config"] = json.loads(data)
    saveAppConfig(jc)

def getEngineConfigFromId(engine_id):
  jc = getJsonConfigFiles('')
  for item in jc:
    # print(item)
    if (item['id'] == engine_id):
      return item
  return {"id" : "ENGINE_NOT_FOUND", "description" : "ENGINE_NOT_FOUND"}
    
      
    


def getEngineConfig(root):
   return getJsonConfigFiles(root)


# Config JSON utils
def getJsonConfigFiles(rootPath):
    # D:\NLP_AI_NER\NER_APP\config\engine_config\*.json
    json_folder_path = os.path.join("D:\\", "NLP_AI_NER", "NER_APP", "config", "engine_config")
    json_files = [x for x in os.listdir(json_folder_path) if x.endswith(".json")]
    json_data = []
    for json_file in json_files:
        json_file_path = os.path.join(json_folder_path, json_file)
        # print('getJsonConfigFiles read:' + json_file_path)
        with open(json_file_path) as file:
            data = json.load(file)
            json_data.append(data)
    
    return json_data


def buildEngineList(jsonConfig):
    engList = []
    for item in jsonConfig:
      # print(item['description'])
      engList.append(item['description'])
    return engList

def getConfigFromDescription(jsonConfig, description):
    for item in jsonConfig:
      if(item['description'] == description):
          return item
    return "Config description not found"


# Trasform a ents
def spacyEnt2Json(text, ents, score):

    print('spacyEnt2Json:', ents)

    data = {}
    index = 1

    # ent.text, ent.label_, ent.start_char

    for token in ents:
        print(token.text, token.label_, token.start_char, token.end_char )
        obj = {}
        obj['entity'] = token.label_
        obj['score'] = score
        obj['index'] = index
        obj['word'] = token.text
        obj['start'] = token.start_char
        obj['end'] = token.end_char

        data[index] = obj

#       json_data = json.dumps(data)
        index = index + 1

    return data




# genera il markdown per la visualizzazione
def makeMarkdown(text, json, config):

    markdown = ''
    last_index = 0
    print('@@@@@@@@@@@@@@@makeMarkdown')
    print(text)
    print(markdown)
    

    for item in json:
        # print(item)
        # print(json[item])
        # print(json[item]["end"])

        print(markdown)

        pos_start = json[item]["start"]
        pos_end = json[item]["end"]
        entity = json[item]["entity"]

        print(pos_start,pos_end,entity)

        markdown += text[last_index:pos_start] + f':red[' + text[pos_start:pos_end] + f'][:blue[' + entity + f']]'
        last_index = pos_end

    # add tail

    markdown += text[last_index:]

    print(markdown)

    print('exit')

    return markdown

# format LMStudio response
def formatLMStudioResponse(r):
    markdown = ''
    last_index = 0
    print("formatLMStudioResponse")
    print(r)

    #"choices": [
    #{
    #  "index": 0,
    #  "message": {
    #    "role": "assistant",
    #    "content": " Nome: Mario Rossi\nCognome: Rossi\nQualifica professionale: Dr. (Dottore)\nNome completo per codice fiscale: Mario Rossi\nCodice fiscale: NRRRSS70E23H294A\nEvento: Convegno\nOrganizzazione: MyCorp Inc.\nCodice identificativo MyCorpo: 00304260409\nLuogo: Roma, in via Salaria 100\nInformazioni di salute: ha il raffreddore e l'influenza\nIndirizzo email: marco.rossi@libero.it"
    #  },
    #  "finish_reason": "stop"
    #}
    #],
    
    json_data = []

    for item in r["choices"]:
      print(item["index"],item["message"])
      msg = item["message"]["content"]
      print(msg)
      list_msg = msg.split("\n")
      print(list_msg)
      for el in list_msg:
         elems = el.split(":",1)
         
         d = 'NOT_FOUND'
         v = 'NOT_FOUND'

         if elems.count(1) > 1:
            d = elems[0].strip()
            v = elems[1].strip()
           

         json_data.append({
            "description" : d,
            "value" : v
         })
      print(json_data)
    

    return json_data













'''

:red[TEXT2BOLD][:blue[LOC]] NoColor :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].


for ent in entities:
  k = ent["entity_group"]
  print(k)
  if styles[ent["entity_group"]]:
    style = styles[ent["entity_group"]]
  else:
    style = styles[ent["DEFAULT"]]
  ann_text += text[last_index:ent["start"]] + f'<span style="{style}">' + text[ent["start"]:ent["end"]] + '[' + k + ']' + f'</span>'
  last_index = ent["end"]
  print(last_index, text[ent["start"]:ent["end"]])

print("----------------------------------------------------------------------------------------")
print(text)
print("----------------------------------------------------------------------------------------")

# IPython.display.HTML(ann_text)

display(IPython.display.HTML(ann_text))

'''

# Spacy version
def json2DataFrame(j):
  jc = json.dumps(j , cls=CustomEncoder)
  data = json.loads(jc)
  # df = pd.json_normalize(data)
  df = pd.DataFrame(data).T
  return df

# Hugging Face version & LMStudio
def json2DataFrameHF(j):
  df = pd.json_normalize(j)
  return df

# Json Patch from key int to string ...
def jsonPatchHF(j):

  dataList = []
  data = {}
  # data['key'] = 'value'
  # json_data = json.dumps(data)

  print(j)
  i = 0

  for item in j:
    print(i, item)
    data = {}
    data[str(i)] = item
    dataList.append(item)
    i = i + 1
  
  return json.dumps(dataList)

# patch per il valore dello score decimale
def jsonPatchScoreField(j):
  data = []
  # data['key'] = 'value'
  # json_data = json.dumps(data)

  for item in j:
    item["score"] = str(item["score"])
    data.append(item)
  
  return json.dumps(data)
 
# patch per normalizzare il risultato si Spacy in Json
def jsonSpacy(j):
  data = []
  # data['key'] = 'value'
  # json_data = json.dumps(data)

  for item in j:
    print(item)
    print(j[item])
    # item["score"] = str(item["score"])
    data.append(j[item])
  
  return data
   