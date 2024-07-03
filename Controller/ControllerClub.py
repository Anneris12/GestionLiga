from View.ViewClub import ViewClub
from Model.Club import Club


class ControllerClub:
    def __init__(self):
        self.vista = ViewClub()
        self.listaClubes = []

    def cargarClubes(self):
        with open("Archivos/clubes.txt") as file:
            renglones = file.readlines()
            for i in renglones:
                codigo, denominacion = i.strip().split(",")
                self.listaClubes.append(Club(codigo, denominacion))

    def mostrarListadoClubes(self):
        self.vista.listar(self.listaClubes)

    def buscarCodigo(self, codigo):
        for o in self.listaClubes:
            if (o.codigo == codigo):
                return o

    def listarJugadoresPorClub(self, club, lista):
        lista = club.getListaJugadores(lista)
        self.vista.listar(lista)
