
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
- HuggingFace (vari modelli NER)
- LLM vari attraverso LMStudio (Mistral, LLAMa 2,3 ed altri)

Il risultato è un report che evidenza i dati personali nel testo.

## Installazione 

- TODO

## Guida 

- TODO

## Riferimenti, risorse ed informazioni

[Garante Privacy, informazioni](https://www.garanteprivacy.it/home/diritti/cosa-intendiamo-per-dati-personali) garanteprivacy.it

[I dati sensibili](https://gdprlab.it/dati-sensibili-e-gdpr-quali-sono-e-come-trattarli-a-norma-di-legge/) gdprlab.it


[GDPR definizione dati personali - Commissione Europeaa](https://commission.europa.eu/law/law-topic/data-protection/reform/what-personal-data_it)

[Microsoft Presidio](https://microsoft.github.io/presidio/) It provides fast identification and anonymization modules for private entities in text and images such as credit card numbers, names, locations, social security numbers, bitcoin wallets, US phone numbers, financial data and more.

[Spacy](https://spacy.io/) Industrial-Strength
Natural Language
Processing

[Hugging Face](https://huggingface.co/) The platform where the machine learning community collaborates on models, datasets, and applications.


[LMStudio](https://lmstudio.ai/) Permette di eseguire LLM in locale.

[Streamlit](https://streamlit.io/)A faster way to build and share data apps


