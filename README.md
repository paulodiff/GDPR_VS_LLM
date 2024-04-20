
# GDPR_VS_LLM

## La storia 

# In un mondo ideale tutti potevano usare i dati di tutti con gli LLM

![Copilot: Genera un'immagine così descritta: in primo piano si vede una persona seduta ad un computer. Sullo schermo del computer su sfondo bianco c'è un testo nero "LLM".
Sullo sfondo ci sono una chiavetta usb, un floppy disk, un cdrom, una nuvola collegati da una scia di un flusso dati che entra nel computer della persona.](STORIA_1.png)


# Un giorno arrivò GDPR e bloccò tutto per garantirne la riservatezza

![Copilot: Genera un'immagine così descritta: in primo piano si vede una persona seduta ad un computer. Sullo sfondo ci sono una chiavetta usb, un floppy disk, un cdrom, una nuvola collegati da una scia di un flusso dati che entra nel computer della persona.](STORIA_2.png)

# Ma un piccolo ragazzo risolse tutto creando un software "GDPR_vs_LLM"


![Copilot:Genera un'immagine così descritta: un super eroe digitale, con una maglietta con un logo rosso con il testo "GDPR" taglia con un'ascia tutti i collegamenti fra una postazione pc ed una nuvola](STORIA_3.png)


# La morale!

>  Prima di usare un LLM controlliamo i dati che inviamo!


# Cos'è GDPR_VS_LLM

## Un software eseguito in locale (sul proprio pc) che cerca di trovare ed evidenziare i dati personali che non dovremmo inviare ad un LLM (come ChatGPT, Gemini, Bart, Copilot, Mistral ecc ...) durante le richieste ...

# Come funziona ?

Il testo viene analizzato da diversi motori di analisi del testo specializza in [NER](https://en.wikipedia.org/wiki/Named-entity_recognition):

- Spacy (List, RegularExpression, NER Model)
- HuggingFace (Model 1 .. )
- LLM vari attraverso LMStudio (Mistral et altri)

Il risultato è un report che evidenza i dati personali nel testo con

## Riferimenti e risorse

Garante Privacy
https://www.garanteprivacy.it/home/diritti/cosa-intendiamo-per-dati-personali
https://gdprlab.it/dati-sensibili-e-gdpr-quali-sono-e-come-trattarli-a-norma-di-legge/


GDPR definizione dati personali - Commissione Europeaa
https://commission.europa.eu/law/law-topic/data-protection/reform/what-personal-data_it

Microsoft Presidio https://microsoft.github.io/presidio/
Piattaforma già predisposta per questa analisi, integra diverse tecnologie, ottimo candidato, già completo analizza immagini ed altro

Spacy https://spacy.io/
Libreria per l'analisi del testo completa anche con modelli NLP

Hugging Face https://huggingface.co/
Modelli NER di pubblico dominio per l'analisi del testo

LMStudio


## Idea generale
Prima bozza una software con UI [StreamLite](https://streamlit.io/) per l'analisi di un testo da copia incolla che come output segnala gli eventuali dati personali 
Avere molteplici analisi con modelli diversi con pesi diversi per un

