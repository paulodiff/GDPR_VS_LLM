# GDPR_VS_LLM
GDPR versus LLM prima di usare un LLM controlliamo i dati che inviamo!

## Un software eseguito in locale (sul proprio pc) che cerca di trovare ed evidenziare i dati personali che non dovremmo inviare ad un LLM (come ChatGPT, Gemini, Bart ...) durante le richieste ...

## Alcune idee

# Garante Privacy
https://www.garanteprivacy.it/home/diritti/cosa-intendiamo-per-dati-personali


# Microsoft Presidio https://microsoft.github.io/presidio/
Piattaforma già predisposta per questa analisi, integra diverse tecnologie, ottimo candidato, già completo analizza immagini ed altro

# Spacy https://spacy.io/
Libreria per l'analisi del testo completa anche con modelli NLP

# Hugging Face https://huggingface.co/
Modelli NER di pubblico dominio per l'analisi del testo

## Idea generale
Prima bozza una software con UI [StreamLite](https://streamlit.io/) per l'analisi di un testo da copia incolla che come output segnala gli eventuali dati personali 
Avere molteplici analisi con modelli diversi con pesi diversi per un
