
import streamlit as st
import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')

st.title('Named Entity Recognition')

text = st.text_area('Please, Enter a Text to Extract Entities')


def entity_recognition(text):
    document = nlp(text)
    entities = [(ent.text, ent.label_) for ent in document.ents]
    return entities

def show_entities(document):
    json = displacy.render(document, style = 'ent', jupyter=False)
    return json

if st.button('Extract Entities'):
    if text:
        document = nlp(text)
        entities = entity_recognition(text)
        st.write(entities)
        st.subheader('Extracted Entities:')
        st.markdown(show_entities(document), unsafe_allow_html= True)
