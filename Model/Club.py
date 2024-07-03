class Club:
    def __init__(self, codigo, denominacion):
        self.codigo = codigo
        self.denominacion = denominacion
    def getListaJugadores(self, lista):
        listaJugadoresxClub=[]
        for i in lista:
            if (i.club.codigo== self.codigo):
                listaJugadoresxClub.append(i)
        return listaJugadoresxClub


    def __str__(self):
        return self.codigo + " - " + self.denominacion

    def __repr__(self):
        return self.codigo + " - " + self.denominacion