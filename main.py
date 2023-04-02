from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str

app = FastAPI()
app.title = "Movies API"
app.version = "0.0.1"

# Movies
movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'
    },
    {
        'id': 2,
        'title': 'Clockwork Orange',
        'overview': "Loquitos",
        'year': '2008',
        'rating': 7.8,
        'category': 'Acción'
    },
    {
        'id': 3,
        'title': 'Shutter Island',
        'overview': "Mas loquitos y DiCaprio",
        'year': '2006',
        'rating': 7.8,
        'category': 'Acción'
    }
]


@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1>Blyat</h1>')


@app.get('/movies', tags=['Movies'])
def get_movies():
    return movies


@app.get('/movies/{id}', tags=['Movies'])
def get_movies(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return []


@app.get('/movies/',  tags=['Movies'])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies if item['category'] == category]


@app.post('/movies', tags=['Movies'])
def create_movie(movie: Movie):
    movies.append(movie)


@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, movie: Movie):
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category   
            return movies
