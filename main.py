import os
import tmdbsimple as tmdb

import productora

tmdb.API_KEY = "b4bf9b38aa8253a44598435f8fb13000";

while True:
    os.system("cls");

    print("""bienvenido a infoshowmov
    [0] Buscar una pelicula
    [1] Buscar una serie
    [2] Buscar un actor o actriz
    [3] mostrar top 10 peliculas 
    [4] mostrar top 10 series
    [5] Exit
    """);
    opcion = input("dime una opcion: ");

    if opcion == "0":
      print(productora.buscarpelicula(input("busca una pelicula: ")));
    elif opcion == "1":
      print(productora.buscarShow(input("busca una serie: ")));
    elif opcion == "2":
      print(productora.buscar_actores(input("busca un actor/actriz: ")));
    elif opcion == "3":
      print(productora.top_peliculas());
    elif opcion == "4":
      print(productora.top_series());
    else:
      exit(0);

    os.system("pause");



        
