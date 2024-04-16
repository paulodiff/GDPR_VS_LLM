import requests

class LMStudioEngine(): 
      
    def __init__(self, json_config, text_2_analyze): 
        print('Init LMStudioEngine:')
        print(json_config)
        self.engine_config = json_config 
        self.text_2_analyze = text_2_analyze

    def run(self): 
        
        print("LM Engine config:", self.engine_config["payload"]) 

        payload = self.engine_config["payload"]
        print("LM Engine text:", payload) 

        payload_prompt = payload["prompt"]
        
        payload_prompt = payload_prompt.replace("{txt}", self.text_2_analyze)

        payload["prompt"] = payload_prompt

        payload["messages"][1] = {
            "role":"user",
            "content": payload_prompt
        }

        URL = self.engine_config["apiUrl"]
        
        # x = txt.replace("bananas", "apples")

                
        r = requests.post(url=URL, json=payload)
        
        data = r.json()

        print('LMStudioEngine:response')        

        print(data)

               
        
        
        return data