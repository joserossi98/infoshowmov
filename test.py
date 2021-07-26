import requests
import json


API_KEY = 'b4bf9b38aa8253a44598435f8fb13000'


nombrePelicula = str(input("Dame un nombre de una pelicula"))

nombrePelicula.replace(" ", "%20")

response = requests.get('https://api.themoviedb.org/3/search/movie?api_key='+ API_KEY +'&language=en-US&query='+ nombrePelicula +'&page=1&include_adult=false')

pelicula = response.json()

id = pelicula["results"][0]['id']

response = requests.get('https://api.themoviedb.org/3/movie/'+ str(id) +'?api_key='+ API_KEY +'&language=en-US')

pelicula = response.json()

titulo = pelicula['original_title']
descripcion = pelicula['overview']
anno = pelicula['release_date']

response = requests.get('https://api.themoviedb.org/3/movie/'+ str(id) +'/credits?api_key='+ API_KEY +'&language=en-US')
pelicula = response.json()

actores = []

for actor in pelicula['cast',3]:
    actores.append(actor['name'])

print("Titulo:\t" + titulo)
print("Descripcion:\t" + descripcion)
print("Anno de lanzamiento:\t" + anno)
print("Actores: ")

for actor in actores:
    print(actor)
