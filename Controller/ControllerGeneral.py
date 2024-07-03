from View.ViewGeneral import ViewGeneral
from Controller.ControllerClub import ControllerClub
from Controller.ControllerCategoria import ControllerCategoria
from Controller.ControllerJugador import ControllerJugador


class ControllerGeneral:
    def __init__(self):
        self.vista = ViewGeneral(self)
        self.controllerClub = ControllerClub()
        self.controllerCategoria = ControllerCategoria()
        self.controllerJugador = ControllerJugador(self.controllerClub, self.controllerCategoria)

    def cargarDesdeArchivo(self):
        #cargarClubes
        self.controllerClub.cargarClubes()
        #cargarCategorias
        self.controllerCategoria.cargarCategorias()
        # cargarJugadores
        self.controllerJugador.cargarJugadores()

    def iniciar(self):
        self.cargarDesdeArchivo()
        self.vista.main()
        """op = self.vista.eleccionMenuPrincipal()
        # MenuPrincipal
        while (op != "0"):
            if (op == "1"):
                #MostrarListadoDeJugadores
                self.controllerJugador.mostrarListaJugadores()
            elif (op == "2"):
                #RegistrarJugador
                self.controllerJugador.registrarJugador()
            elif (op == "3"):
                #Mostrar jugadores por club
                self.controllerClub.mostrarListadoClubes()
                codigo=self.vista.solicitarDato("codigo del club: ")
                objeto=self.controllerClub.buscarCodigo(codigo)
                self.controllerClub.listarJugadoresPorClub(objeto,self.controllerJugador.listaJugadores)
            elif (op == "4"):
                #Mostrar desempeño de jugadores
                self.controllerJugador.mostrarDesempDeJugadores()
            elif (op == "5"):
                #Consultar jugadores por categoria y club
                self.controllerClub.mostrarListadoClubes()
                codigoClub = self.vista.solicitarDato("codigo del club:")
                objetoClub = self.controllerClub.buscarCodigo(codigoClub)
                self.controllerCategoria.mostrarListadoCategorias()
                codigoCat = self.vista.solicitarDato("codigo de la categoria: ")
                objetoCat = self.controllerCategoria.buscarCodigo(codigoCat)
                self.controllerJugador.listarJugadoresPorClubYCategoria(objetoClub,objetoCat)
            elif (op == "6"):
                #Mostrar la cantidad de jugadores por categoria
                self.controllerCategoria.mostrarListadoCategorias()
                codigo = self.vista.solicitarDato("codigo del club: ")
                objeto = self.controllerCategoria.buscarCodigo(codigo)
                self.controllerCategoria.cantidadJugadoresPorCategoria(objeto, self.controllerJugador.listaJugadores)
            elif (op == "7"):
                #Filtrar por categoria y mostrar jugador y club perteneciente
                self.controllerCategoria.mostrarListadoCategorias()
                codigo = self.vista.solicitarDato("codigo del club: ")
                objeto = self.controllerCategoria.buscarCodigo(codigo)
                self.controllerCategoria.detallarJugadorPorCategoria(objeto,self.controllerJugador.listaJugadores)
            elif (op == "0"):
                #Salir
                break
            else:
                self.vista.opcionIncorrecta()
            op = self.vista.eleccionMenuPrincipal()"""
