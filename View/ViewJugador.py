class ViewJugador:
    def listar(self, lista):
        print(lista)

    def ingresarDato(self, nombreDato):
        return input(f"Ingrese el {nombreDato}: ")

    def mostrar(self, info):
        print(info)

    def listarDetallado(self, listaJugadoresClubCat,objetoClub,objetoCat):
        print(f"Club: {objetoClub.denominacion} - Categoria: {objetoCat.denominacion}")
        for i in listaJugadoresClubCat:
            print(i.getMostrarInfoDetallado())

        print(f"La cantidad de jugadores es: {len(listaJugadoresClubCat)}")