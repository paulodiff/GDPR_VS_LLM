# Analyze text and return data

import utils.utils as ut
import utils.SpacyEngine as SE
import utils.TransformerEngine as TE

def TextAnalyzer(text, config, options):

    print('TextAnalyzer')
    print(config)
    print(options)

    result = []

    for item in options:
        print('Start Text Analyzer with description: ' + item)
        json_config = ut.getConfigFromDescription(config, item)
        engine = json_config['engine']

        print('Start Text Analyzer with engine: ' + engine)
  
        if engine == 'spacy':
            eng = SE.SpacyEngine(json_config, text)
            data =  eng.run()
            result.append({
                "engine" : engine,
                "description" : item,
                "data" : data
            })
            
        elif engine == 'Transformer':

            result.append({
                "engine" : engine,
                "description" : item,
                "data" : []
            })

        else: 
            result.append({
                "engine" : engine,
                "description" : 'NOT FOUND!',
                "data" : []
            })
            


    return result


def ReRankResponse(r):
    print('TextAnalyzer')
    return []


        

