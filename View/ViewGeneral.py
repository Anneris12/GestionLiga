class ViewGeneral:
    def eleccionMenuPrincipal(self):
        print("Menu Principal: "
              "\n1-Mostrar listado de jugadores"
              "\n2-Registrar jugador"
              "\n3-Mostrar jugadores por club"
              "\n4-Mostrar desempeño de jugadores"
              "\n5-Consultar jugadores por categoria y club"
              "\n6-Mostrar la cantidad de jugadores por categoria"
              "\n7-Filtrar por categoria y mostrar jugador y club perteneciente"
              "\n8-Salir")
        op=input("Elija la opcion que desee: ")
        return op

    def opcionIncorrecta(self):
        print("La opcion ingresada es incorrecta.")

    def solicitarDato(self, param):
        return input (f"Ingrese el {param} ")