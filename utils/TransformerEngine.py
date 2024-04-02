from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

class TransformerEngine(): 
      
    def __init__(self, json_config, text_2_analyze): 
        self.engine_config = json_config 
        self.text_2_analyze = text_2_analyze

    def run(self): 
        
        model_name = self.engine_config["model_name"]
        print("TransformerEngine text:", model_name) 
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForTokenClassification.from_pretrained(model_name)
        nlp = pipeline("ner", model=model, tokenizer=tokenizer)
        ner_results = nlp(self.text_2_analyze)
        return ner_results