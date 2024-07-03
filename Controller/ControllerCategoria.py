from View.ViewCategoria import ViewCategoria
from Model.Categoria import Categoria
class ControllerCategoria:
    def __init__(self):
        self.vista=ViewCategoria()
        self.listaCategorias=[]

    def cargarCategorias(self):
        with open("Archivos/categorias.txt") as file:
            renglones = file.readlines()
            for i in renglones:
                codigo, denominacion = i.strip().split(",")
                self.listaCategorias.append(Categoria(codigo, denominacion))

    def mostrarListadoCategorias(self):
        self.vista.listar(self.listaCategorias)

    def buscarCodigo(self, codigoCat):
        for o in self.listaCategorias:
            if (o.codigo == codigoCat):
                return o

    def cantidadJugadoresPorCategoria(self, objeto, listaJugadores):
        self.vista.mostrarInfo(objeto.getCantidadJugadores(listaJugadores))

    def detallarJugadorPorCategoria(self, objeto, listaJugadores):
        self.vista.mostrarInfo(objeto.denominacion)
        self.vista.listarDetallado(objeto.getListaJugadores(listaJugadores))


    
