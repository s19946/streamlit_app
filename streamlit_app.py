import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os

st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')

if st.button('Kliknij'):
     st.error('Błąd, nie wolno klikać nieznanych rzeczy!') 

st.title('Aplikacja- tłumaczenie tekstów')

st.write('Ta niesamowita aplikacja wyprowadzi Cię z angielskiego świata i wprowadzi Cię do niemieckiego świata. Guten tag!')

st.header('Tłumaczenie tekstów z angielskiego na niemiecki')

st.info('Wprowadź poniżej teskt po angielsku')
import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "Opcje",
    [
        "Tłumacz tekst",
        "Wydźwięk emocjonalny tekstu (eng)",
    ],
)

if option == "Wydźwięk emocjonalny tekstu (eng)":
    text = st.text_area(label="Wpisz tekst")
    if text:
        classifier = pipeline("sentiment-analysis")
        answer = classifier(text)
        st.write(answer)
elif option == "Tłumacz tekst":
    text = st.text_area(label="Wpisz tekst po angielsku")
    if text:
        classifier = pipeline("translation_en_to_de")
        answer = classifier(text)
        st.write("Przetłumaczony tekst: " + answer[0]['translation_text'])

st.spinner()
with st.spinner(text='Working...'):
    time.sleep(2)
    st.success('Done')
    
st.subheader('Indeks: s19946')

st.subheader('Zadanie do wykonania')
st.write('Wykorzystaj Huggin Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Huggin Face - https://huggingface.co/transformers/usage.html')
st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?')
st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
st.write('🐞 Na końcu umieść swój numer indeksu')
st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')
