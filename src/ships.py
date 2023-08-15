class Ship:
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
        weight=self.draft-self.crew*Ship.crewWeight
        return weight

class Cruise(Ship):
    passengersWeight=2.25
    def __init__(self, draft, crew, passengers=0):#pongo 0 por defecto por si no me pasan nada
        super().__init__(draft,crew)
        self.passengers = passengers
      ##  try:
        ##    ship.check_type(draft)
       ##     ship.check_type(crew)
       ##     ship.check_type(passengers)
       ## except ValueError:
        ##    return


    def calculate_weight(self):
        weight=self.draft-self.crew*Ship.crewWeight-self.passengers*Cruise.passengersWeight
        return

class Cargo (Ship):
    # statics de los valores correspondientes a cada calidad de cargo
    value_quality1 = 3.5
    value_quality05 = 2
    value_quality025 = 0.5
    def __init__(self, draft, crew, cargo=0, quality=0):
        super().__init__(draft, crew)
        self.cargo = cargo
        self.quality = quality
    def calculate_weight(self):
        cargo_aux=0
        if(self.quality==1):
            cargo_aux= self.value_quality1
        elif (self.quality==0.5):
            cargo_aux= self.value_quality05
        elif(self.quality==0.25):
            cargo_aux= self.value_quality025
        else:
            raise ValueError("Valor de calidad invalido")

        weight=self.draft-self.crew*Ship.crewWeight-self.cargo*cargo_aux
        return weight