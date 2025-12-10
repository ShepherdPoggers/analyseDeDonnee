import streamlit as st
import pandas as pd
import plotly.express as px
from includes.loadGraph import filmSerie, genres, paysProducteur, evolutionFilmSeries, boxPlot

@st.cache_data
def chargerDonnee():
    """La fonction chargerDonnee permmet de charger le dataSet avec pandas"""
    df = pd.read_csv("analyseNetflix/data/netflix_titles.csv")
    df = nettoyage(df)
    return df
    
def nettoyage(df : pd.DataFrame):
    """nettoyage permet de nettoyer le dataSet (même code que dans le jupyterNoteBook)"""
    cols_a_remplir = ["director", "cast", "country", "rating", "duration"]
    df[cols_a_remplir] = df[cols_a_remplir].fillna("Unknown")

    # Conversion de la colonne 'date_added' en datetime
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

    # Retrait des espaces au début et à la fin des chaînes
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    
    return df

def loadPage():
    """Permet de charger la page streamlit"""
    st.set_page_config(
        page_title="Analyse Netflix",
        layout="wide"
    )

    st.title("Analyse des contenus Netflix - 8PRO408")
    st.markdown("Par Olivier Séguin, Elliot Shepherd et Olivier Robin")
    st.subheader("Graphiques intéressants")
    df = chargerDonnee()
    filmSerie(df)
    genres(df)
    paysProducteur(df)
    evolutionFilmSeries(df)
    boxPlot(df)


if __name__ == "__main__":
    loadPage()