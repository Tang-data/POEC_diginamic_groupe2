

from pymongo import MongoClient
import pandas as pd
import streamlit as st
from art import *

#Configuration des dimensions & affichage de la page
st.set_page_config(page_title="Projet MongoDB",
                   page_icon=":books:",
                   layout='wide')

st.markdown("""
<iframe src="https://docs.google.com/presentation/d/1k5bYijMriwp7vVOY3-yZ50brLUCD2XmvC44rWp-35BY/embed?start=false&loop=false&delayms=3000" width="1250" height="900"></iframe>
""", unsafe_allow_html=True)


# # Fonction titre centré
# def centered_text(text, taille):
#     st.markdown(f"<{taille} style='text-align: center;'>{text}</h3>", unsafe_allow_html=True)
#     st.write("\n")
# # Conversion du titre en ASCII art
# texte = text2art("Bienvenue",font="Caligraphy")
# # Affichage titre
# st.markdown(f"```{texte}```")
# st.title("sur l'application de gestion de votre Bibliothèque :books:")
# texte=":books:"
# centered_text("< == Veuillez choisir un onglet sur la gauche de votre écran", "h3")
