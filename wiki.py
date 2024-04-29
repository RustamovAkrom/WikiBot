import wikipedia
from settings import WIKIPEDIA_SET_LANGUAGE


def wiki_summary_searching(search: str):
    wikipedia.set_lang(WIKIPEDIA_SET_LANGUAGE.lower())

    try:
        response = wikipedia.summary(search)
        return response
    except:
        return "Bu mavzuga oid maqola topa olmadim!. Iltimos boshqa narsa kiriting."
    
    