
class ship:
    crewWeight = 1.5
    def check_type(value):
        if type(value)==int or type(value)==float:
            return True
        else:
            raise ValueError("El valor ingresado no es un numero")
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        aux=self.calculate_weight
        if(aux>20):
            print("El barco merece ser saqueado")
        else:
            raise ValueError("Error de cantidad")
        return aux
        # SINTAXIS DEL TRY
        # try:
           # loquesea()
        # except ValueError as e:
            # print(e.args) //imprime "Error de cantidad"

    def calculate_weight(self):
        weight=self.draft-self.crew*ship.crewWeight
        return weight

    #en el csv la primer columna es de draft, la segunda de crew, la tercera de cargo y la cuarta de quality.
    #para saber de q clase es el objeto hay q ver cuantas columnas estan llenas en esa fila (2 ship, 3 cruise, 4 cargo).
    #algunas tienen quality pero no cargo, raro.