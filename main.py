import os
import tmdbsimple as tmdb

tmdb.API_KEY = ''

#escoger lenguaje 
# input 1 para espanol y 2 para ingles
lenguaje = int(input("1 para espanol y 2 para ingles"))

dictEspanol = {
  "bienvenido": "bienvenido al app que bucas peliculas!",
  "model": "Mustang",
  "year": 1964
}

dictIngles = {
  "bienvenido": "Welcome to my app",
  "model": "Mustang",
  "year": 1964
}


while True:
    os.system("cls");

    print("""bienvenido a infoshowmov
    [0] Buscar una pelicula/serie/actor/actriz
    [1] mostrar top 10 peliculas 
    [2] mostrar top 10 series
    """);
    opcion = input("dime una opcion");
    os.system("pause");

        
