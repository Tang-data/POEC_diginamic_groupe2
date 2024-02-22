import pymongo
from pymongo import MongoClient
import pandas as pd
import streamlit as st
import time

#Configuration des dimensions & affichage de la page
st.set_page_config(page_title="Ajout d'un Ouvrage",
                   page_icon=":heavy_plus_sign:",
                   layout='wide')

# Fonction titre centré
def centered_text(text):
    st.markdown(f"<h3 style='text-align: center;'>{text}</h3>", unsafe_allow_html=True)
    st.write("\n")
centered_text("Ajouter un Ouvrage")

# Fonction pour créer un délai
def s(time_to_sleep):
    time.sleep(int(time_to_sleep))

# import DB
client = MongoClient()
db = client.MongoDB
Books = db.Books_1000


##### AJOUT D'UN OUVRAGE #####

st.title("\n Veuillez indique le titre, le ou les auteurs, l'année de parution ainsi que le format de votre ouvrage : \n")


# titre
titre = st.text_input("\n Titre de l'ouvrage : \n")

# auteur
auteurs= []
nb_auteurs = st.number_input("Combien d'Auteurs voulez-vous ajouter ?", value=0, step=1)

for auteur in range(nb_auteurs):
    auteur = st.text_input(f"\n Veuillez saisir le nom de l'auteur N°{auteur+1} : \n")
    auteurs.append(auteur)
    
# annee
annee = st.number_input("\n Année de parution de l'ouvrage : \n", value=2024, step=1)

# type
liste_formats = ["Article", "Livre", "Thèse", "Autre"]
format = st.selectbox(
    'format', liste_formats, index=liste_formats.index('Article')
    )
if format == "Autre":
    format = st.text_input("\n Entrez le format de votre ouvrage : \n")

# id
try:
    if titre is not None:
        if auteur is not None:
            id = f"{format}{annee}{titre[0]}{auteur[0][0]}"
except:
    pass


# Bouton de validation
if st.button("Valider"):
    Books.insert_one({
        "_id": id,
        "type": format,
        "title": titre,
        "year": annee,
        "authors": auteurs
    })

    s(1)
    st.write("\n L'ouvrage a bien été ajouté à la base \n")
    st.balloons()