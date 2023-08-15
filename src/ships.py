
class Ship:
    crewWeight = 1.5

    def convert_type(value) -> float:
        try:
            aux = float(value)
        except ValueError as e:
            print(e.args)
        else:
            if aux >= 0:
                return aux
        raise ValueError("El valor ingresado no es valido")
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self)->float:
        try:
            aux=self.calculate_weight()
        except ValueError as e:
            print(e.args)
        else:
            if(aux>20.0):
                print("El barco merece ser saqueado")
            else:
                raise ValueError("Error de cantidad")
            return aux

    def calculate_weight(self)->float:
        aux_draft=Ship.convert_type(self.draft)
        aux_crew=Ship.convert_type(self.crew)
        weight=aux_draft-aux_crew*Ship.crewWeight
        return weight

class Cruise(Ship):
    passengersWeight=2.25
    def __init__(self, draft, crew, passengers=0):#pongo 0 por defecto por si no me pasan nada
        super().__init__(draft,crew)
        self.passengers = passengers

    def calculate_weight(self)->float:
        aux_draft=Ship.convert_type(self.draft)
        aux_crew=Ship.convert_type(self.crew)
        aux_passengers=Ship.convert_type(self.passengers)
        weight=aux_draft-aux_crew*Ship.crewWeight-aux_passengers*Cruise.passengersWeight
        return weight

class Cargo (Ship):
    # statics de los valores correspondientes a cada calidad de cargo
    value_quality1 = 3.5
    value_quality05 = 2
    value_quality025 = 0.5
    def __init__(self, draft, crew, cargo=0, quality=0):
        super().__init__(draft, crew)
        self.cargo = cargo
        self.quality = quality
    def calculate_weight(self)->float:
        aux_draft = Ship.convert_type(self.draft)
        aux_crew = Ship.convert_type(self.crew)
        aux_cargo=Ship.convert_type(self.cargo)
        cargo_aux_val=0
        quality_aux=Ship.convert_type(self.quality)
        if(quality_aux==1):
            cargo_aux_val= Cargo.value_quality1
        elif (quality_aux==0.5):
            cargo_aux_val= Cargo.value_quality05
        elif(quality_aux==0.25):
            cargo_aux_val= Cargo.value_quality025
        else:
            raise ValueError("Valor de calidad invalido")
        weight=aux_draft-aux_crew*Ship.crewWeight-aux_cargo*cargo_aux_val
        return weight