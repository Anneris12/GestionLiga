class Categoria:
    def __init__(self, codigo, denominacion):
        self.codigo = codigo
        self.denominacion = denominacion

    def getCantidadJugadores(self, lista):
        return len(self.getListaJugadores(lista))

    def getListaJugadores(self,lista):
        listaJugadoresCategoria=[]
        for i in lista:
            if (i.categoria.codigo == self.codigo):
                listaJugadoresCategoria.append(i)
        return listaJugadoresCategoria

    def __str__(self):
        return self.codigo + " - " + self.denominacion

    def __repr__(self):
        return self.codigo+" - "+self.denominacion