import requests
import json

from requests.models import Response

API_KEY = 'b4bf9b38aa8253a44598435f8fb13000';

def guardar():
    pass;

def cargar():
    pass;


#peliculas
def buscarpelicula(nombrepelicula):
#obtenemos id de la pelicula
    response = requests.get('https://api.themoviedb.org/3/search/movie?api_key='+ API_KEY +'&language=en-US&query='+ nombrepelicula +'&page=1&include_adult=false')
    pelicula = response.json();
    id = pelicula["results"][0]['id'];
    
     #Obtenemos el nombre, descripcion y anno de lanzamiento
    response = requests.get('https://api.themoviedb.org/3/movie/'+ str(id) +'?api_key='+ API_KEY +'&language=en-US');
    pelicula = response.json();

    nombrepelicula = pelicula['original_title'];
    descripcion = pelicula['overview'];
    anno_lanzamiento = pelicula['release_date'];

    #obtenemos el cast
    response = requests.get('https://api.themoviedb.org/3/movie/'+ str(id) +'/credits?api_key='+ API_KEY +'&language=en-US')
    pelicula = response.json()

    actores = []
    for actor in pelicula['cast']:
        actores.append(actor['name'])

    return f"Nombre: {nombrepelicula}\nDescripcion: {descripcion}\nAnno de lanzamiento: {anno_lanzamiento}\nCast: {actores}"

#series
def buscarShow(nombreshow):
    #Obtenemos el id del tv show
    response = requests.get('https://api.themoviedb.org/3/search/tv?api_key='+ API_KEY +'&language=en-US&page=1&query='+ nombreshow +'&include_adult=false');
    serie = response.json();
    id = serie["results"][0]['id'];

    #obtenemos el nombre, descripcion, temporadas y capitulos
    response = requests.get('https://api.themoviedb.org/3/tv/'+ str(id) +'?api_key='+ API_KEY +'&language=en-US');
    serie = response.json();
    nombreshow = serie['original_name'];
    descripcionSerie = serie['overview'];
    temporadas = serie['number_of_seasons'];
    capitulos = serie['number_of_episodes'];

    #Obtenemos el cast
    response = requests.get('https://api.themoviedb.org/3/tv/'+ str(id) +'/credits?api_key='+ API_KEY +'&language=en-US');
    serie = response.json();
    actoresSerie = [];

    for actor in serie['cast']:
        actoresSerie.append(actor['name'])
    
    return f"Titulo: {nombreshow}\nDescripcion: {descripcionSerie}\nTemporada: {temporadas}\nCapitulos: {capitulos}\nCast: {actoresSerie}"   

#actores
def buscar_actores(actores):
    #obtenemos id de actor/actriz
    response = requests.get('https://api.themoviedb.org/3/search/person?api_key='+ API_KEY +'&language=en-US&query='+ actores +'&include_adult=false')
    nombre_actores = response.json();
    id = nombre_actores['results'][0]['id']

    #obtenemos el nombre del actor/actriz y peliculas y series en las aparece
    response = requests.get('https://api.themoviedb.org/3/person/'+ str(id) +'/combined_credits?api_key='+ API_KEY +'&language=en-US');
    actores = response.json();
    participaciones = "";

    for actor in actores['cast']:
        if 'original_title' in actor:
            participaciones += actor['original_title'] + "\n";
        elif 'original_name' in actor:
            participaciones += actor['original_name'] + "\n";
        

    return f"{participaciones}"

   
#top 10 peliculas y series
def top_series():
    response = requests.get('https://api.themoviedb.org/3/tv/top_rated?api_key='+ API_KEY +'&language=en-US&page=1');
    top = response.json();
    top10series = top['results'];
    lista_series = "";

    for series in top10series:
        lista_series += series['original_name'] + "\n";

    return f"{lista_series}\n";

def top_peliculas():
    response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key='+ API_KEY +'&language=en-US&page=1');
    top = response.json();
    top10peliculas = top['results'];
    lista_peliculas = "";

    for peliculas in top10peliculas:
        lista_peliculas += peliculas['original_title'] + "\n";

    return f"{lista_peliculas}\n";

