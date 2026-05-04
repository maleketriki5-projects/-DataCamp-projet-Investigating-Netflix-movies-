# Importer les packets pandas et  matplotlib
import pandas as pd   #pd est l'alias de pandas
import matplotlib.pyplot as plt   # plt est l'alias du module pyplot
# Définitions:
# Pandas est une bibliothèque(paquete) utilisée pour manipuler, analyser et nettoyer des données sous forme de tableaux (DataFrame).

# Matplotlib est une  paquete de base en Python qui contient dans son module pyplot tous les outils pour dessiner des graphiques, des shemas pour but la visualisation
# de données. Le code est l'outil, et le graphique est le résultat qui montre ce que les données racontent.

# Lecture du Netflix CSV (fichier data) comme une DataFrame( tableau de données)
netflix_df = pd.read_csv("netflix_data.csv")

# Filtrer les films des années 90 (1990 à 1999)
movies_90 = netflix_df[(netflix_df["type"] == "Movie") & (netflix_df["release_year"] >= 1990) & (netflix_df["release_year"] < 2000)]

# Filtrer le data de netflix autrefois pour garder seulement "Movie" de type "Action"
action_movies = movies_90[movies_90["genre"] == "Action"]

# Filtrer les films d'action des années 90 qui durent moins de 90 minutes
short_action_movies = action_movies[action_movies["duration"] < 90]

# Compter le nombre de ces films
short_movie_count=len(short_action_movies)

# Afficher le résultat final
print("Nombre de films d'action courts :", short_movie_count)

# Afficher les 5 premiers films de ta liste filtrée
print(short_action_movies.head())




