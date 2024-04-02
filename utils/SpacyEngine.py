import spacy
import utils.utils as ut
from spacy.matcher import Matcher

class SpacyEngine(): 
      
    def __init__(self, json_config, text_2_analyze): 
        print('SpacyEngine init!')
        self.engine_config = json_config 
        self.text_2_analyze = text_2_analyze
          
    def run(self): 
        print("Engine config:", self.engine_config) 
        print("Engine text:", self.text_2_analyze) 

        spacy_type = self.engine_config["type"]

        print("Engine run Spacy type:", spacy_type)

        if spacy_type == 'LIST':
            
            print('Engine Spacy data', self.engine_config["lists"])

            nlp = spacy.load("en_core_web_sm")
            nlp.disable_pipes('ner')
            ruler = nlp.add_pipe("entity_ruler")

            # creating rules patterns
            patterns = []
            for list_item in self.engine_config["lists"]:
                # pattern = [{"LOWER": "hello"}, {"IS_PUNCT": True}, {"LOWER": "world"}]
                pattern = list_item["data"]
                label = list_item["label"]
                patterns.append({
                       "label" : label,
                       "pattern" : [{"LEMMA": {"IN": pattern}}]
                })

            print(patterns)
            ruler.add_patterns(patterns)
            doc = nlp(self.text_2_analyze)
            
            print(doc.ents)
            print([(ent.text, ent.label_, ent) for ent in doc.ents])

            response = ut.spacyEnt2Json(self.text_2_analyze, doc.ents, 1)

            return response
        
        elif spacy_type == 'REGEXP':

            print('Engine Spacy data', self.engine_config["lists"])

            nlp = spacy.load("en_core_web_sm")
            nlp.disable_pipes('ner')
            ruler = nlp.add_pipe("entity_ruler")

            # creating rules patterns
            patterns = []
            for list_item in self.engine_config["lists"]:
                # {"label": "PI_", "pattern": [{"TEXT" : {"REGEX": "^[0-9]{11}$"}}]},
                pattern = list_item["data"]
                label = list_item["label"]
                patterns.append({
                       "label" : label,
                       "pattern" : [{"TEXT": {"REGEX": pattern}}]
                })

            print(patterns)
            ruler.add_patterns(patterns)
            doc = nlp(self.text_2_analyze)
            
            print(doc.ents)
            print([(ent.text, ent.label_, ent) for ent in doc.ents])

            response = ut.spacyEnt2Json(self.text_2_analyze, doc.ents, 1)

            return response

        
        elif spacy_type == 'NER':

            print('Engine Spacy data NER')
            nlp = spacy.load("it_core_news_lg")
            doc = nlp(self.text_2_analyze)
            response = ut.spacyEnt2Json(self.text_2_analyze, doc.ents, 1)
            return response
        
        else: 
            print("Spacy type NOT not Found!:", spacy_type)
            return []

'''
        nlp = spacy.load("en_core_web_sm")
        matcher = Matcher(nlp.vocab)
        # Add match ID "HelloWorld" with no callback and one pattern
        pattern = [{"LOWER": "hello"}, {"IS_PUNCT": True}, {"LOWER": "world"}]

        print("Engine text:", self.text_2_analyze) 

        matcher.add("HelloWorld", [pattern])

        doc = nlp("Hello, world! Hello world!")
        matches = matcher(doc)
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]  # Get string representation
            span = doc[start:end]  # The matched span
            print(match_id, string_id, start, end, span.text)

        return ('SpacyEngine:show')
''' 