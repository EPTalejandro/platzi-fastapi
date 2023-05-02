from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
import db
from pydantic import BaseModel
from typing import Optional
from copy import deepcopy

app=FastAPI()
#al cambiar el atributo title de nuestro objeto 'FastAPI' se cambia el titulo de la documentacion
app.title = 'mi primera app'
#el atributo version cambiar como se muestra esta puede tener utilidad combinado con GIT 
app.version = '0.0.1'

class Movies(BaseModel):
    id:Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str

#la ruta '/' vendria siendo la ruta raiz de nuestra api
@app.get('/', tags=['home'])
def message():
    return "hola mundo"

@app.get('/movies', tags=['movies'])
def movies():
    return db.data

@app.get('/movies/{id}', tags=['movies'])
def get_movies(id: int):
    movie = list(filter(lambda x: x['id'] == id,db.data))
    return movie[0] if len(movie) > 0 else f'No hay una pelicula con ese ID == {id}'

#al dejar un espacio libre luedo de '/' tendremos lugar a posibles parametros queary
#los cuales son definidos en los inputs de la funcion en este caso "Category"
@app.get('/movies/', tags=['movies'])
def get_by_category(category: str):
    movies = list(filter(lambda item: item['category'] == category,db.data))
    return movies if len(movies) > 0 else f'No hay peliculas de esa categoria {category}'

@app.post('/movies', tags=['movies'])
def add_movie(movie: Movies):
    new_movie = movie.dict()
    db.add_data(new_movie)
    return db.data

@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    movie = [movie for movie in db.data if movie['id'] == id]
    if len(movie) == 0:
        return f"No hay ninguna pelicula con el id: {id}"
    db.delete_data(id)
    return f"la pelicula {movie[0]['title']} con el id {id} a sido eliminada", db.data

@app.put('/update/{id}')
def update_movies(id:int, movie_to_update: Movies):
    old_movie = [movie for movie in db.data if movie['id'] == id]
    old_movie_copy = deepcopy(old_movie[0])
    movie_to_update.id = id
    db.update_data(id, movie_to_update.dict())
    return {'old_data':old_movie_copy,
            'new_data':movie_to_update}

