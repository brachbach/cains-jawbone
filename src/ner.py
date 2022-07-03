import spacy

nlp = spacy.load('en_core_web_trf')

BLACKLISTED_ENTITY_TYPES=["ORDINAL", "CARDINAL", "QUANTITY", "DATE", "TIME"]

def ner(text: str) -> list[str]:
    doc = nlp(text)
    entities = [entity.text for entity in doc.ents if not entity.label_ in BLACKLISTED_ENTITY_TYPES]
    return entities