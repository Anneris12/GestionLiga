class Jugador:
    def __init__(self,dni,apeNom,club,categoria,goles,amones,expul):
        self.dni=dni
        self.apeNom=apeNom
        self.club=club
        self.categoria=categoria
        self.goles=goles
        self.amones=amones
        self.expul=expul

    def getMostrarInfoDetallado(self):
        return f"Ape y Nom: {self.apeNom} - Club: {self.club.denominacion} - Goles: {self.goles} - Am: {self.amones} - Ex: {self.expul}"
    def getPuntosDesemp(self):
        return int(self.goles)*10 - int(self.amones)*2 - int(self.expul)*5

    def getDatosDesemp(self):
        return f"{self.apeNom} - {self.club.denominacion} - {self.categoria.denominacion} - {self.getPuntosDesemp()}"

    def __str__(self):
        return self.dni + " - " + self.apeNom

    def __repr__(self):
        return self.dni + " - " + self.apeNom