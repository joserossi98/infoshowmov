class movies():
    def __init__(self, nombrepelicula, descripcion, anno_lanzamiento, actores):
        self.nombrepelicula = nombrepelicula;
        self.descripcion = descripcion;
        self.dia_lanzamiento = anno_lanzamiento;
        self.actores = actores;

    def __repr__(self):
        return f"{self.nombrepelicula}\t\t{self.descripcion}\t\t{self.dia_lanzamiento}\t\t{self.actores}";

class shows():
    def __init__(self, nombreshow, descripcionSerie, temporadas, capitulos, actoresSerie):
        self.nombreshow = nombreshow;
        self.descripcionSerie = descripcionSerie;
        self.temporadas = temporadas;
        self.capitulos = capitulos;
        self.actoresSerie = actoresSerie;
    
    def __repr__(self):
        return f"{self.nombreshow}\t\t{self.descripcionSerie}\t\t{self.temporadas}\t\t{self.capitulos}\t\t{self.actoresSerie}";
        