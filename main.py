from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import pandas as pd
import operator
from api import presentacion
from fastapi.responses import JSONResponse
import json

app = FastAPI()

result = pd.read_parquet('result.parquet')
data = pd.read_parquet('games_reviews_items.parquet')

@app.get(path="/", 
         response_class=HTMLResponse,
         tags=["Home"])
def home():
    '''
    Hola comunidad Henry, para mi un gusto mostrar el desarrollo de las funciones solicitadas.
    Gracias por estar acá.

    '''
    return presentacion()

@app.get(path = '/PlayTimeGenre')
def PlayTimeGenre(genero: str):
    
    genre_data = data[data['genres'] == genero]

    
    year_playtime = genre_data.groupby('release_year')['playtime_forever'].sum()

    
    year_with_most_playtime = year_playtime.idxmax()

    return {"Año de lanzamiento con más minutos jugados para Género {}: {}".format(genero, year_with_most_playtime)}     


@app.get(path = '/UseForGenre')
def UserForGenre(genero: str):
    
    genre_data = data[data['genres'] == genero]

    
    user_with_most_playtime = genre_data.groupby('user_id')['playtime_forever'].sum().idxmax()

    
    user_most_playtime_data = genre_data[genre_data['user_id'] == user_with_most_playtime]

    
    playtime_by_year = [{"Año": year, "Minutos": hours} for year, hours in user_most_playtime_data.groupby('release_year')['playtime_forever'].sum().reset_index().values]

    result = {
        f"Usuario con más minutos jugados para Género {genero}: {user_with_most_playtime}": playtime_by_year
    }

    return result




@app.get(path = '/UserRecommend')
def UsersRecommend(año: int):
    
    filtered_data = data[(data['posted_year'] == año) & (data['recommend'] == True) & (data['sentiment_analysis'].isin([1, 2]))]

    game_recommendations = filtered_data.groupby('title')['recommend'].count().reset_index()

    game_recommendations = game_recommendations.sort_values(by='recommend', ascending=False)

    top_3_games = game_recommendations.head(3)

    results = [{"Puesto {}: {}".format(i + 1, game)} for i, game in enumerate(top_3_games['title'])]

    return results


@app.get(path = '/UsersNotRecommend')
def UsersNotRecommend(año: int):
    
    filtered_data = data[(data['posted_year'] == año) & (data['recommend'] == False) & (data['sentiment_analysis'] == 0)]

    game_not_recommendations = filtered_data.groupby('title')['recommend'].count().reset_index()

    game_not_recommendations = game_not_recommendations.sort_values(by='recommend', ascending=False)

    top_3_games = game_not_recommendations.head(3)

    results = [{"Puesto {}: {}".format(i + 1, game)} for i, game in enumerate(top_3_games['title'])]

    return results






@app.get(path = '/Sentiment_analysis')
def sentiment_analysis(year: str):
     

     reviews_year = data[data['release_year'] == year]
    

     sentiment_counts = {'Negative': 0, 'Neutral': 0, 'Positive': 0}
    

     for _, row in reviews_year.iterrows():
         sentiment = row['sentiment_analysis']
         sentiment_category = ''
        

         try:

             if sentiment == 0:
                 sentiment_category = 'Negative'
             elif sentiment == 1:
                 sentiment_category = 'Neutral'
             elif sentiment == 2:
                 sentiment_category = 'Positive'
            

             sentiment_counts[sentiment_category] += 1
         except ValueError:

             pass
    
     return sentiment_counts







@app.get("/obtener_recomendaciones_por_item_id/{item}")
def obtener_recomendaciones_por_item_id(item: int):
    recomendaciones = result[result['item_id'] == item]['recommended'].iloc[0]
    
    if len(recomendaciones) > 0:
        recomendaciones_dict = {i + 1: juego for i, juego in enumerate(recomendaciones)}
        return recomendaciones_dict
    else:
        
        error_data = {'error': 'No se encontraron recomendaciones para el ID proporcionado'}
        return JSONResponse(content=error_data, status_code=404)