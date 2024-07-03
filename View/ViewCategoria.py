class ViewCategoria:
    def listar(self, lista):
        print(lista)

    def mostrarInfo(self, info):
        print(info)

    def listarDetallado(self, lista):
        for i in lista:
            print(i.getMostrarInfoDetallado())