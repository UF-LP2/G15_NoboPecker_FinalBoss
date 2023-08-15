from src.class_ship import ship
class cargo (ship):
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

        weight=self.draft-self.crew*ship.crewWeight-self.cargo*cargo_aux
        return weight