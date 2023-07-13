import streamlit as st
import pandas as pd


# Definimos las columnas que nos interesan
fields = ['country','title', 'points', 'price', 'variety']

# Cargamos el DataFrame sólo con esas columnas
df = pd.read_csv('wine_reviews.csv', usecols=fields)
df.dropna(inplace=True)

if st.checkbox("Mostrar dataframe"):
    st.dataframe(df)

if st.checkbox("Vista de datos Head o Tail"):
    if st.button('Tu Ofertón Personalizado'):
        st.write(df.sample(1))

st.radio('Dimensión a mostrar:',('Filas','Columnas'))



