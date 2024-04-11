import streamlit as st
import os
import subprocess
import pandas as pd
import numpy as np
import utils.utils as ut
import random


def add_engine_button():
    print(">>>ADD ENGINE BUTTON!..")
    print(optionEngine)
    ut.updateAppConfigAddEngine(optionEngine)

def save_button():
    print(">>>SAVE BUTTON!..")
    print(df_config_editor)
    df2save = df_config_editor[['engine_id', 'enable']]
    json_string = df2save.to_json(orient='records')  
    print("json data to save:")
    print(json_string)
    ut.updateAppConfig(json_string)
    
    



st.set_page_config(
     page_title='NER_APP',
     layout="wide",
     initial_sidebar_state="expanded",
)

print('>>>START - PAGE')

st.write("appConfigFile:", st.secrets.app.appConfigFile)





st.header("Configuration manager")

st.text("Pagina di configurazione dove è possibile abilitare o disabilitare i vari motori di analisi:")

print('>>>Loading config')
engine_config_json = ut.getEngineConfig('dummy')
app_config_json = ut.getAppConfig('dummy')

# st.json(app_config_json)
# print(app_config_json)

df_config = []
engine_ids = []


#if 'df' not in st.session_state:
#    st.session_state.df = pd.DataFrame(data=pd.read_csv("data/data.csv"))

# create and display engine config
for item in app_config_json["engine_config"]:
    # print(item)
    # print(item['engine_id'])
    
    engine_config = ut.getEngineConfigFromId(item['engine_id'])
    # print(engine_config)

    engine_ids.append(item['engine_id'])
    df_config.append(
        {
            "engine_id" : item["engine_id"],
            "description": engine_config["description"],
            "enable" : item["enable"],
            "remove" : False,
        }
    )

# st.session_state.df_engine_config.reset_index(drop=True, inplace=True)
    
# st.json(app_config_json)

print(df_config)

st.text("Engine configurati:")
df1 = pd.DataFrame(df_config)
df_config_editor = st.data_editor(df1, 
                           use_container_width=True,
                           key="df_config_editor",
                           column_config={
                                "engine_id": "Engine ID",
                                "description": "Engine desc",
                                "enable" : "Engine enabled",
                                "remove" : "Remove Engine",
                                 },
                            disabled=["engine_id", "description"],
                            num_rows="fixed",
                            hide_index=False
                           )
st.button('Save data', on_click=save_button)

# print(df_config_editor)
# print(df1)
# print(st.session_state)
st.text("Engine disponibili:")

# st.text(engine_ids)

# create and display engine available
list_engine_available = []
for item in engine_config_json:
    if(item["id"] not in engine_ids):
        list_engine_available.append(item["id"])
      


optionEngine = st.selectbox('Engine da aggiungere a quelli configurati',list_engine_available)

st.button('Aggiungi Engine',  on_click=add_engine_button)
    

#
#df = pd.DataFrame(
#    [
#       {"command": "st.selectbox", "rating": 4, "is_widget": True},
#       {"command": "st.balloons", "rating": 5, "is_widget": False},
#       {"command": "st.time_input", "rating": 3, "is_widget": True},
#   ]
#)


# favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]



# st.json(engine_config_json)


