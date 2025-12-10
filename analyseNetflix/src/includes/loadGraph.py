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
    
def paysProducteur(df: pd.DataFrame):
    """Permet l'affichage du top 20 pays producteurs"""
    
    # Séparer les pays multiples
    countries = df['country'].dropna().str.split(", ", expand=True).stack()

    # Top 20
    country_counts = countries.value_counts().head(20).reset_index()
    country_counts.columns = ["country", "count"]   # noms uniformes

    # Bar chart
    fig = px.bar(
        country_counts,
        x="country",
        y="count",
        title="Top 20 pays producteurs",
        text="count"
    )
    fig.update_layout(
        xaxis_tickangle=-45
    )

    # Carte choroplèthe interactive
    fig2 = px.choropleth(
        country_counts,
        locations="country",         # noms des pays
        locationmode="country names",
        color="count",
        hover_name="country",
        color_continuous_scale="Viridis",
        title="Top 20 des pays producteurs (Carte interactive)"
    )

    # Affichage Streamlit
    st.plotly_chart(fig, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)
    
def evolutionFilmSeries(df: pd.DataFrame):
    """Cette fonction permet l'affichage du line chart du nombre de films et séries sortis par année"""

    # Agrégation
    dfYearType = (
        df.groupby(["release_year", "type"])["show_id"]
        .count()
        .reset_index()
    )

    # Line chart interactif
    fig = px.line(
        dfYearType,
        x="release_year",
        y="show_id",
        color="type",
        markers=True,
        title="Films et Séries sortis par année",
        labels={
            "release_year": "Année",
            "show_id": "Nombre de titres",
            "type": "Type"
        }
    )

    fig.update_layout(
        hovermode="x unified"
    )
    
    # Affichage Streamlit
    st.plotly_chart(fig, use_container_width=True)

def boxPlot(df : pd.DataFrame):
    """Peremt de charger un boxplot"""
    #4.7 — Analyse de la durée des films


    # Extraire uniquement les films depuis le dataset complet
    movies = df[df["type"] == "Movie"].copy()

    # Conversion de la colonne 'duration' en nombre de minutes
    # Exemple : "90 min" → 90
    movies["duration_min"] = movies["duration"].str.extract(r"(\d+)").astype(float)

    # Création du boxplot interactif avec Plotly
    fig = px.box(
        movies,
        y="duration_min",        # Axe Y : durée en minutes
        points="all",            # Affiche tous les points individuels pour visualiser les outliers
        title="Distribution des durées des films sur Netflix",
        labels={"duration_min": "Durée en minutes"}  # Renommage de l'axe Y
    )
    st.plotly_chart(fig, use_container_width=True)
