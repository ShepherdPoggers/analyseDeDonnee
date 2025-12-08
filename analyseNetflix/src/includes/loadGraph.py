import streamlit as st
import pandas as pd
import plotly.express as px

def filmSerie(df : pd.DataFrame):
    """Cette fonction permet l'affichage du plot de la répartitionFilmSerie"""
    type_counts = df["type"].value_counts().reset_index()
    type_counts.columns = ["type", "count"]

    fig_type = px.bar(
        type_counts,
        x = "type",
        y = "count",
        text = "count",
        title = "Répartition : Films vs Séries"
    )
    st.plotly_chart(fig_type, use_container_width=True)
    
    
def genres(df : pd.DataFrame):
    """Cette fonction permet l'affichage du plot de la répartition des genres"""
    genres = (
        df["listed_in"]
        .dropna()
        .str.split(",", expand=True)
        .stack()
        .str.strip()
    )
    
    genre_counts = genres.value_counts()
    top_genres = genre_counts.head(15).reset_index()
    top_genres.columns = ["Genre", "Occurrences"]

    fig = px.bar(
        top_genres,
        x = "Genre",
        y = "Occurrences",
        title = "Top 15 des genres les plus fréquents",
        text = "Occurrences"
    )

    fig.update_layout(
        xaxis_tickangle=-45
    )

    st.plotly_chart(fig, use_container_width=True)
    
def paysProducteur(df : pd.DataFrame):
    """Permet l'affichage du top 20 pays producteurs"""
    countries = df['country'].str.split(", ", expand=True).stack()
    country_counts = countries.value_counts().head(20).reset_index()
    country_counts.columns = ["Pays", "Nombre de productions"]
    fig = px.bar(
        country_counts,
        x = "Pays",
        y = "Nombre de productions",
        title = "Top 20 pays producteurs",
        text = "Nombre de productions"
    )
    fig.update_layout(
        xaxis_tickangle=-45
    )

    
    st.plotly_chart(fig, use_container_width=True)
