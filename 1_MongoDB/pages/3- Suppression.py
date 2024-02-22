import pymongo
from pymongo import MongoClient
import pandas as pd
import streamlit as st
import time

#Configuration des dimensions & affichage de la page
st.set_page_config(page_title="Suppression d'Ouvrages",
                   page_icon=":x:",
                   layout='wide')

# Fonction titre centré
def centered_text(text):
    st.markdown(f"<h3 style='text-align: center;'>{text}</h3>", unsafe_allow_html=True)
    st.write("\n")
centered_text("Suppression d'Ouvrages")

# Fonction pour créer un délai
def s(time_to_sleep):
    time.sleep(int(time_to_sleep))

# import DB
client = MongoClient()
db = client.MongoDB
Books = db.Books_1000



##### SUPPRESSION D'UN OUVRAGE #####

st.title("\n Veuillez sélectionner sur votre gauche comment vous voulez sélectionner le ou les ouvrage(s) à supprimer de la bibliothèque\n")


# SIDEBAR


# Choix du Mode de Suppression
supp = st.sidebar.radio(
    "Comment voulez-vous supprimer ?",
    ('Par Id', "Par Titre", 'Par Auteur'))

# Par ID
if supp == 'Par Id':
    ouvrage_supp = st.text_input("\n Saisissez l'identifiant de l'ouvrage à supprimer : \n")
    # Bouton de validation
    if st.button("Valider"):
        Books.delete_one(
            {
            "_id": ouvrage_supp
            }
        )
        s(1)
        st.write("\n L'ouvrage a bien été supprimé de la base \n")
        st.balloons()
        
# Par Titre
elif supp == 'Par Titre':
    st.write("\n Sélectionnez l'ouvrage que vous voulez supprimer : \n")
    liste_titres = []
    for item in Books.find({"title" : {"$regex":"", "$options": "i"}}).sort('title') :
        liste_titres.append(item['title'])
    liste_titres.sort()
    liste_titres.append('Tous')
    titre_supp = st.selectbox(
    'Titre', liste_titres, index=liste_titres.index('Tous')
    )
    if st.button("Valider"):
        Books.delete_one(
            {
            "title": titre_supp
            }
        )
        s(1)
        st.write("\n L'ouvrage a bien été supprimé de la base \n")
        st.balloons()


# Par Auteur
elif supp == 'Par Auteur' :
    st.write("\n Sélectionnez l'auteur dont vous voulez supprimer les ouvrages : \n")
    
    set_auteurs = set([])
    for item in Books.find({"authors" : {"$regex":"", "$options": "i"}}).sort('authors') :
        for i in range (len(item['authors'])) :
            item['authors'][i] = item['authors'][i].replace('?','')
            set_auteurs.add(item['authors'][i])
    liste_auteurs = list(set_auteurs)
    liste_auteurs.sort()
    liste_auteurs.append('Tous')
    auteur_supp = st.selectbox(
    'Auteur', liste_auteurs, index=liste_auteurs.index('Tous')
    )
    if st.button("Valider"):
        for item in Books.aggregate([
            { "$unwind": "$authors"},
            {"$match" : {"authors" : auteur_supp} }
            ]):
            Books.delete_one(
                {
                "authors": auteur_supp
                }
            )
        s(1)
        st.write(f"\n Tous les ouvrages correspondant à {auteur_supp} ont bien été supprimés de la base \n")
        st.balloons()
