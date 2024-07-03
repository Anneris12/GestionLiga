from View.ViewJugador import ViewJugador
from Model.Jugador import Jugador
class ControllerJugador:
    def __init__(self,controllerClub,controllerCategoria):
        self.vista=ViewJugador()
        self.listaJugadores=[]
        self.controllerClub=controllerClub
        self.controllerCategoria=controllerCategoria

    def cargarJugadores(self):
        with open("Archivos/jugadores.txt") as file:
            renglones = file.readlines()
            for i in renglones:
                dni, apeNom,codigoClub,codigoCat,goles,amones,expul = i.strip().split(",")
                objetoClub=self.controllerClub.buscarCodigo(codigoClub)
                objetoCat=self.controllerCategoria.buscarCodigo(codigoCat)
                self.listaJugadores.append(Jugador(dni, apeNom,objetoClub,objetoCat,goles,amones,expul))

    def mostrarListaJugadores(self):
        self.vista.listar(self.listaJugadores)

    def registrarJugador(self):
        dni=self.vista.ingresarDato("DNI")
        apeNom=self.vista.ingresarDato("Apellido y Nombre")
        self.controllerClub.mostrarListadoClubes()
        codClub=self.vista.ingresarDato("codigo del club")
        self.controllerCategoria.mostrarListadoCategorias()
        codCate=self.vista.ingresarDato("codigo de la categoria")
        goles=self.vista.ingresarDato("numero de goles")
        amones=self.vista.ingresarDato("numero de amonestaciones")
        expul=self.vista.ingresarDato("numero de expulsiones")
        objetoClub=self.controllerClub.buscarCodigo(codClub)
        objetoCat=self.controllerCategoria.buscarCodigo(codCate)
        self.listaJugadores.append(Jugador(dni,apeNom,objetoClub,objetoCat,goles,amones,expul))

    def mostrarDesempDeJugadores(self):
        for i in self.listaJugadores:
            self.vista.mostrar(i.getDatosDesemp())

    def listarJugadoresPorClubYCategoria(self, objetoClub, objetoCat):
        listaJugadoresClubCat=[]
        for i in self.listaJugadores:
            if(i.club.codigo == objetoClub.codigo and i.categoria.codigo == objetoCat.codigo):
                listaJugadoresClubCat.append(i)
        self.vista.listarDetallado(listaJugadoresClubCat,objetoClub,objetoCat)